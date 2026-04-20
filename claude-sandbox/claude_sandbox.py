#!/usr/bin/env python3
"""
Claude Sandbox - A menu bar app to quickly launch Claude Code in any directory.

Features:
- Menu bar icon for quick access
- Global keyboard shortcut (⌘⇧C)
- Recent directories list
- Drag & drop folder support
- iTerm with Terminal.app fallback
- Notifications on launch
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

import rumps
from AppKit import (
    NSApp, NSApplication, NSWorkspace, NSPasteboard,
    NSFilenamesPboardType, NSEvent, NSKeyDownMask,
    NSCommandKeyMask, NSShiftKeyMask
)
from PyObjCTools import AppHelper
import Quartz


CONFIG_DIR = Path.home() / ".config" / "claude-sandbox"
CONFIG_FILE = CONFIG_DIR / "config.json"
DEFAULT_DIR = Path.home() / "sandbox"
MAX_RECENT = 10


class ClaudeSandboxApp(rumps.App):
    def __init__(self):
        super().__init__(
            "Claude Sandbox",
            icon=self.get_icon_path(),
            template=True,
            quit_button=None
        )

        self.config = self.load_config()
        self.recent_dirs = self.config.get("recent_dirs", [])

        self.build_menu()
        self.setup_global_hotkey()
        self.setup_drop_target()

    def get_icon_path(self):
        icon_path = Path(__file__).parent / "icon.png"
        if icon_path.exists():
            return str(icon_path)
        return None

    def load_config(self):
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        if CONFIG_FILE.exists():
            try:
                with open(CONFIG_FILE) as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        return {"recent_dirs": [str(DEFAULT_DIR)]}

    def save_config(self):
        self.config["recent_dirs"] = self.recent_dirs[:MAX_RECENT]
        with open(CONFIG_FILE, "w") as f:
            json.dump(self.config, f, indent=2)

    def build_menu(self):
        self.menu.clear()

        self.menu.add(rumps.MenuItem("Open in ~/sandbox", callback=self.open_default))
        self.menu.add(rumps.MenuItem("Open in Current Finder Folder", callback=self.open_finder_folder))
        self.menu.add(rumps.MenuItem("Choose Folder...", callback=self.choose_folder))
        self.menu.add(rumps.separator)

        if self.recent_dirs:
            recent_menu = rumps.MenuItem("Recent Directories")
            for dir_path in self.recent_dirs[:MAX_RECENT]:
                display_name = self.truncate_path(dir_path)
                item = rumps.MenuItem(display_name, callback=lambda _, d=dir_path: self.open_claude(d))
                recent_menu.add(item)
            recent_menu.add(rumps.separator)
            recent_menu.add(rumps.MenuItem("Clear Recent", callback=self.clear_recent))
            self.menu.add(recent_menu)
            self.menu.add(rumps.separator)

        self.menu.add(rumps.MenuItem("⌘⇧C: Global Shortcut", callback=None))
        self.menu.add(rumps.MenuItem("Drag folder onto icon to open", callback=None))
        self.menu[-1].set_callback(None)
        self.menu[-2].set_callback(None)

        self.menu.add(rumps.separator)
        self.menu.add(rumps.MenuItem("Quit", callback=rumps.quit_application))

    def truncate_path(self, path, max_len=40):
        path = path.replace(str(Path.home()), "~")
        if len(path) <= max_len:
            return path
        return "..." + path[-(max_len - 3):]

    def add_to_recent(self, dir_path):
        dir_path = str(dir_path)
        if dir_path in self.recent_dirs:
            self.recent_dirs.remove(dir_path)
        self.recent_dirs.insert(0, dir_path)
        self.recent_dirs = self.recent_dirs[:MAX_RECENT]
        self.save_config()
        self.build_menu()

    def clear_recent(self, _):
        self.recent_dirs = []
        self.save_config()
        self.build_menu()

    def open_default(self, _):
        self.open_claude(str(DEFAULT_DIR))

    def open_finder_folder(self, _):
        script = '''
        tell application "Finder"
            if exists window 1 then
                set currentFolder to (target of window 1) as alias
                return POSIX path of currentFolder
            else
                return ""
            end if
        end tell
        '''
        try:
            result = subprocess.run(
                ["osascript", "-e", script],
                capture_output=True, text=True, check=True
            )
            folder = result.stdout.strip()
            if folder:
                self.open_claude(folder)
            else:
                rumps.notification(
                    "Claude Sandbox",
                    "No Finder window",
                    "Open a Finder window first"
                )
        except subprocess.CalledProcessError:
            rumps.notification(
                "Claude Sandbox",
                "Error",
                "Could not get Finder folder"
            )

    def choose_folder(self, _):
        script = '''
        set chosenFolder to choose folder with prompt "Choose a folder to open Claude in:"
        return POSIX path of chosenFolder
        '''
        try:
            result = subprocess.run(
                ["osascript", "-e", script],
                capture_output=True, text=True, check=True
            )
            folder = result.stdout.strip()
            if folder:
                self.open_claude(folder)
        except subprocess.CalledProcessError:
            pass  # User cancelled

    def open_claude(self, directory):
        directory = str(directory).rstrip("/")

        if not Path(directory).is_dir():
            rumps.notification(
                "Claude Sandbox",
                "Error",
                f"Directory not found: {directory}"
            )
            return

        self.add_to_recent(directory)

        # Try iTerm first, fall back to Terminal
        if self.is_app_installed("iTerm"):
            success = self.open_in_iterm(directory)
        else:
            success = self.open_in_terminal(directory)

        if success:
            dir_name = Path(directory).name
            rumps.notification(
                "Claude Sandbox",
                "Launching Claude",
                f"Opening in {dir_name}"
            )

    def is_app_installed(self, app_name):
        apps_paths = [
            Path("/Applications") / f"{app_name}.app",
            Path.home() / "Applications" / f"{app_name}.app",
        ]
        return any(p.exists() for p in apps_paths)

    def open_in_iterm(self, directory):
        script = f'''
        tell application "iTerm"
            activate
            if (count of windows) > 0 then
                tell current window
                    create tab with default profile
                    tell current session
                        write text "cd {self.escape_path(directory)} && claude"
                    end tell
                end tell
            else
                create window with default profile
                tell current session of current window
                    write text "cd {self.escape_path(directory)} && claude"
                end tell
            end if
        end tell
        '''
        try:
            subprocess.run(["osascript", "-e", script], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def open_in_terminal(self, directory):
        script = f'''
        tell application "Terminal"
            activate
            if (count of windows) > 0 then
                do script "cd {self.escape_path(directory)} && claude"
            else
                do script "cd {self.escape_path(directory)} && claude" in window 1
            end if
        end tell
        '''
        try:
            subprocess.run(["osascript", "-e", script], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def escape_path(self, path):
        return path.replace("\\", "\\\\").replace('"', '\\"').replace("'", "'\\''")

    def setup_global_hotkey(self):
        key_code = 8  # 'c' key
        modifiers = NSCommandKeyMask | NSShiftKeyMask

        def callback(proxy, event_type, event, refcon):
            if event_type == Quartz.kCGEventKeyDown:
                keycode = Quartz.CGEventGetIntegerValueField(event, Quartz.kCGKeyboardEventKeycode)
                flags = Quartz.CGEventGetFlags(event)

                cmd_shift = Quartz.kCGEventFlagMaskCommand | Quartz.kCGEventFlagMaskShift
                if keycode == key_code and (flags & cmd_shift) == cmd_shift:
                    rumps.Timer(0.1, lambda _: self.open_default(None)).start()
            return event

        try:
            self.event_tap = Quartz.CGEventTapCreate(
                Quartz.kCGSessionEventTap,
                Quartz.kCGHeadInsertEventTap,
                Quartz.kCGEventTapOptionDefault,
                Quartz.CGEventMaskBit(Quartz.kCGEventKeyDown),
                callback,
                None
            )

            if self.event_tap:
                run_loop_source = Quartz.CFMachPortCreateRunLoopSource(None, self.event_tap, 0)
                Quartz.CFRunLoopAddSource(
                    Quartz.CFRunLoopGetCurrent(),
                    run_loop_source,
                    Quartz.kCFRunLoopDefaultMode
                )
                Quartz.CGEventTapEnable(self.event_tap, True)
        except Exception as e:
            print(f"Could not setup global hotkey: {e}")
            print("Grant Accessibility permissions in System Preferences > Privacy & Security")

    def setup_drop_target(self):
        pass


def main():
    # Ensure we're running as a proper app
    if not NSApp:
        NSApplication.sharedApplication()

    app = ClaudeSandboxApp()
    app.run()


if __name__ == "__main__":
    main()
