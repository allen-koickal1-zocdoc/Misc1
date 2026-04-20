#!/usr/bin/env python3
"""
Claude Buddy - A walking desktop companion that opens Claude Code on click.
"""

import sys
import random
import subprocess
import math
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer, QPointF
from PyQt6.QtGui import (
    QPainter, QColor, QPen, QBrush, QPainterPath,
    QLinearGradient, QRadialGradient
)


class ClaudeBuddy(QWidget):
    # Character dimensions - taller for realistic proportions
    CHAR_WIDTH = 60
    CHAR_HEIGHT = 120

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)

        self.setFixedSize(self.CHAR_WIDTH + 40, self.CHAR_HEIGHT + 30)

        screen = QApplication.primaryScreen().geometry()
        self.screen_width = screen.width()
        self.screen_height = screen.height()

        self.move(100, self.screen_height - self.CHAR_HEIGHT - 60)

        # Movement
        self.speed = 1.8
        self.walking = True
        self.direction = 1
        self.hovering = False
        self.clicked = False

        # Animation
        self.walk_cycle = 0.0
        self.breath_cycle = 0.0
        self.blink_timer = 0
        self.is_blinking = False

        # Timers
        self.move_timer = QTimer(self)
        self.move_timer.timeout.connect(self.tick)
        self.move_timer.start(16)

        self.behavior_timer = QTimer(self)
        self.behavior_timer.timeout.connect(self.random_behavior)
        self.behavior_timer.start(5000)

    def tick(self):
        if self.walking:
            self.walk_cycle += 0.15
            if self.walk_cycle > 2 * math.pi:
                self.walk_cycle -= 2 * math.pi

            pos = self.pos()
            new_x = pos.x() + (self.speed * self.direction)

            if new_x <= 0:
                self.direction = 1
                new_x = 0
            elif new_x >= self.screen_width - self.width():
                self.direction = -1
                new_x = self.screen_width - self.width()

            self.move(int(new_x), pos.y())

        # Breathing animation (always)
        self.breath_cycle += 0.05
        if self.breath_cycle > 2 * math.pi:
            self.breath_cycle -= 2 * math.pi

        # Blinking
        self.blink_timer += 1
        if self.blink_timer > 180:  # ~3 seconds
            self.is_blinking = True
            if self.blink_timer > 186:
                self.is_blinking = False
                self.blink_timer = random.randint(0, 60)

        self.update()

    def random_behavior(self):
        if self.clicked:
            return
        action = random.choice(["walk", "walk", "walk", "turn", "stop", "go"])
        if action == "turn":
            self.direction *= -1
        elif action == "stop":
            self.walking = False
        elif action == "go":
            self.walking = True

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        cx = self.width() // 2
        ground_y = self.height() - 15

        if self.direction == -1:
            painter.translate(self.width(), 0)
            painter.scale(-1, 1)

        # Animation values
        if self.walking:
            leg_swing = math.sin(self.walk_cycle) * 18
            arm_swing = math.sin(self.walk_cycle) * 15
            body_bob = abs(math.sin(self.walk_cycle * 2)) * 3
            head_tilt = math.sin(self.walk_cycle) * 2
        else:
            leg_swing = 0
            arm_swing = 0
            body_bob = 0
            head_tilt = 0

        breath = math.sin(self.breath_cycle) * 1.5

        # === SHADOW ===
        shadow_gradient = QRadialGradient(cx, ground_y, 25)
        shadow_gradient.setColorAt(0, QColor(0, 0, 0, 60))
        shadow_gradient.setColorAt(1, QColor(0, 0, 0, 0))
        painter.setBrush(shadow_gradient)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(cx - 25, ground_y - 5, 50, 12)

        # === LEGS ===
        # Back leg (darker)
        self.draw_leg(painter, cx + 6, ground_y - 45 - body_bob, -leg_swing, ground_y, is_back=True)
        # Front leg
        self.draw_leg(painter, cx - 6, ground_y - 45 - body_bob, leg_swing, ground_y, is_back=False)

        # === TORSO ===
        torso_top = ground_y - 75 - body_bob
        torso_bottom = ground_y - 42 - body_bob

        # Shirt with gradient
        shirt_gradient = QLinearGradient(cx - 15, torso_top, cx + 15, torso_bottom)
        shirt_gradient.setColorAt(0, QColor(65, 105, 160))
        shirt_gradient.setColorAt(0.5, QColor(70, 130, 180))
        shirt_gradient.setColorAt(1, QColor(55, 95, 140))

        painter.setBrush(shirt_gradient)
        painter.setPen(Qt.PenStyle.NoPen)

        torso = QPainterPath()
        torso.moveTo(cx - 14, torso_top + 5)
        torso.cubicTo(cx - 16, torso_top + 15, cx - 14, torso_bottom - 5, cx - 10, torso_bottom)
        torso.lineTo(cx + 10, torso_bottom)
        torso.cubicTo(cx + 14, torso_bottom - 5, cx + 16, torso_top + 15, cx + 14, torso_top + 5)
        torso.closeSubpath()
        painter.drawPath(torso)

        # Collar
        painter.setPen(QPen(QColor(50, 80, 120), 1.5))
        collar = QPainterPath()
        collar.moveTo(cx - 8, torso_top + 3)
        collar.quadTo(cx, torso_top + 10, cx + 8, torso_top + 3)
        painter.drawPath(collar)

        # Shirt buttons
        painter.setBrush(QColor(45, 75, 115))
        painter.setPen(Qt.PenStyle.NoPen)
        for i in range(3):
            by = torso_top + 15 + i * 10
            painter.drawEllipse(cx - 2, int(by), 4, 4)

        # === ARMS ===
        arm_top_y = torso_top + 8

        if self.hovering:
            # Waving animation
            self.draw_arm(painter, cx - 14, arm_top_y, -35, -50, is_back=True)
            self.draw_arm(painter, cx + 14, arm_top_y, 35, -50, is_back=False)
        else:
            # Normal arm swing
            self.draw_arm(painter, cx - 14, arm_top_y, -8 + arm_swing * 0.8, 25, is_back=True)
            self.draw_arm(painter, cx + 14, arm_top_y, 8 - arm_swing * 0.8, 25, is_back=False)

        # === NECK ===
        neck_top = torso_top - 5
        painter.setBrush(QColor(245, 205, 165))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(cx - 5, int(neck_top), 10, 12)

        # === HEAD ===
        head_center_y = neck_top - 18
        head_width = 28
        head_height = 32

        # Head shape with gradient for 3D effect
        head_gradient = QRadialGradient(cx - 5, head_center_y - 5, head_width)
        head_gradient.setColorAt(0, QColor(255, 218, 185))
        head_gradient.setColorAt(0.7, QColor(245, 200, 160))
        head_gradient.setColorAt(1, QColor(225, 180, 140))

        painter.setBrush(head_gradient)

        # Slightly tilted head when walking
        painter.save()
        painter.translate(cx, head_center_y)
        painter.rotate(head_tilt)
        painter.translate(-cx, -head_center_y)

        # Head oval
        painter.drawEllipse(cx - head_width // 2, int(head_center_y - head_height // 2),
                           head_width, head_height)

        # === HAIR ===
        hair_gradient = QLinearGradient(cx - 14, head_center_y - 20, cx + 14, head_center_y)
        hair_gradient.setColorAt(0, QColor(50, 35, 25))
        hair_gradient.setColorAt(0.5, QColor(65, 45, 30))
        hair_gradient.setColorAt(1, QColor(45, 30, 20))

        painter.setBrush(hair_gradient)
        painter.setPen(Qt.PenStyle.NoPen)

        hair = QPainterPath()
        hair.moveTo(cx - 14, head_center_y - 2)
        hair.cubicTo(cx - 16, head_center_y - 12, cx - 10, head_center_y - 20, cx, head_center_y - 18)
        hair.cubicTo(cx + 10, head_center_y - 20, cx + 16, head_center_y - 12, cx + 14, head_center_y - 2)
        hair.cubicTo(cx + 12, head_center_y - 8, cx, head_center_y - 6, cx - 12, head_center_y - 8)
        hair.closeSubpath()
        painter.drawPath(hair)

        # Hair strands
        painter.setPen(QPen(QColor(35, 25, 15), 1))
        painter.drawLine(cx - 8, int(head_center_y - 15), cx - 10, int(head_center_y - 5))
        painter.drawLine(cx + 3, int(head_center_y - 17), cx + 2, int(head_center_y - 8))

        # === FACE ===
        # Ears
        painter.setBrush(QColor(240, 195, 155))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(cx - head_width // 2 - 3, int(head_center_y - 3), 7, 10)
        painter.drawEllipse(cx + head_width // 2 - 4, int(head_center_y - 3), 7, 10)

        # Inner ear
        painter.setBrush(QColor(220, 170, 135))
        painter.drawEllipse(cx - head_width // 2 - 1, int(head_center_y), 4, 6)
        painter.drawEllipse(cx + head_width // 2 - 2, int(head_center_y), 4, 6)

        # Eyebrows
        painter.setPen(QPen(QColor(55, 40, 30), 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        painter.drawLine(cx - 9, int(head_center_y - 3), cx - 4, int(head_center_y - 4))
        painter.drawLine(cx + 4, int(head_center_y - 4), cx + 9, int(head_center_y - 3))

        # Eyes
        eye_y = head_center_y + 2
        if self.is_blinking:
            # Closed eyes
            painter.setPen(QPen(QColor(60, 40, 30), 2))
            painter.drawLine(cx - 9, int(eye_y), cx - 4, int(eye_y))
            painter.drawLine(cx + 4, int(eye_y), cx + 9, int(eye_y))
        else:
            # Eye whites
            painter.setBrush(QColor(255, 255, 255))
            painter.setPen(QPen(QColor(180, 160, 140), 0.5))
            painter.drawEllipse(cx - 10, int(eye_y - 3), 8, 7)
            painter.drawEllipse(cx + 2, int(eye_y - 3), 8, 7)

            # Iris
            painter.setBrush(QColor(85, 60, 40))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(cx - 8, int(eye_y - 2), 5, 5)
            painter.drawEllipse(cx + 4, int(eye_y - 2), 5, 5)

            # Pupils
            painter.setBrush(QColor(20, 15, 10))
            painter.drawEllipse(cx - 7, int(eye_y - 1), 3, 3)
            painter.drawEllipse(cx + 5, int(eye_y - 1), 3, 3)

            # Eye highlights
            painter.setBrush(QColor(255, 255, 255, 200))
            painter.drawEllipse(cx - 8, int(eye_y - 2), 2, 2)
            painter.drawEllipse(cx + 4, int(eye_y - 2), 2, 2)

        # Nose
        painter.setPen(QPen(QColor(210, 170, 140), 1.5))
        nose = QPainterPath()
        nose.moveTo(cx, head_center_y + 2)
        nose.quadTo(cx + 3, head_center_y + 8, cx, head_center_y + 10)
        painter.drawPath(nose)

        # Mouth
        mouth_y = head_center_y + 13
        if self.hovering or self.clicked:
            # Big smile
            painter.setPen(QPen(QColor(180, 90, 80), 2))
            smile = QPainterPath()
            smile.moveTo(cx - 6, mouth_y)
            smile.quadTo(cx, mouth_y + 6, cx + 6, mouth_y)
            painter.drawPath(smile)

            # Teeth hint
            painter.setBrush(QColor(255, 255, 255))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRect(cx - 4, int(mouth_y + 1), 8, 3)
        else:
            # Slight smile
            painter.setPen(QPen(QColor(190, 110, 100), 1.5))
            smile = QPainterPath()
            smile.moveTo(cx - 5, mouth_y)
            smile.quadTo(cx, mouth_y + 3, cx + 5, mouth_y)
            painter.drawPath(smile)

        # Cheek blush
        painter.setBrush(QColor(255, 180, 170, 60))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(cx - 13, int(head_center_y + 5), 6, 4)
        painter.drawEllipse(cx + 7, int(head_center_y + 5), 6, 4)

        painter.restore()  # Restore from head tilt

        # === SPARKLES (when clicked) ===
        if self.clicked:
            self.draw_sparkles(painter, cx, head_center_y - 25)

    def draw_leg(self, painter, x, top_y, swing, ground_y, is_back):
        """Draw a detailed leg with thigh, knee, calf, and shoe."""
        darkness = 0.85 if is_back else 1.0

        # Pants color with shading
        pants_base = QColor(50, 50, 60)
        pants_color = QColor(
            int(pants_base.red() * darkness),
            int(pants_base.green() * darkness),
            int(pants_base.blue() * darkness)
        )

        knee_x = x + swing * 0.3
        knee_y = top_y + 18
        ankle_x = x + swing
        ankle_y = ground_y - 12

        # Thigh
        painter.setPen(QPen(pants_color, 10, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        painter.drawLine(int(x), int(top_y), int(knee_x), int(knee_y))

        # Calf
        painter.setPen(QPen(pants_color, 8, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        painter.drawLine(int(knee_x), int(knee_y), int(ankle_x), int(ankle_y))

        # Shoe
        shoe_color = QColor(int(60 * darkness), int(45 * darkness), int(35 * darkness))
        painter.setBrush(shoe_color)
        painter.setPen(Qt.PenStyle.NoPen)

        shoe = QPainterPath()
        shoe.moveTo(ankle_x - 6, ankle_y)
        shoe.lineTo(ankle_x - 8, ground_y - 3)
        shoe.quadTo(ankle_x, ground_y, ankle_x + 10, ground_y - 2)
        shoe.lineTo(ankle_x + 8, ankle_y)
        shoe.closeSubpath()
        painter.drawPath(shoe)

        # Shoe sole
        painter.setBrush(QColor(30, 25, 20))
        painter.drawRect(int(ankle_x - 7), int(ground_y - 3), 16, 3)

    def draw_arm(self, painter, shoulder_x, shoulder_y, end_offset_x, end_offset_y, is_back):
        """Draw an arm with upper arm, forearm, and hand."""
        darkness = 0.85 if is_back else 1.0

        shirt_color = QColor(
            int(70 * darkness),
            int(130 * darkness),
            int(180 * darkness)
        )
        skin_color = QColor(
            int(245 * darkness),
            int(200 * darkness),
            int(165 * darkness)
        )

        elbow_x = shoulder_x + end_offset_x * 0.4
        elbow_y = shoulder_y + abs(end_offset_y) * 0.5
        hand_x = shoulder_x + end_offset_x
        hand_y = shoulder_y + end_offset_y

        # Upper arm (shirt sleeve)
        painter.setPen(QPen(shirt_color, 8, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        painter.drawLine(int(shoulder_x), int(shoulder_y), int(elbow_x), int(elbow_y))

        # Forearm (skin)
        painter.setPen(QPen(skin_color, 6, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
        painter.drawLine(int(elbow_x), int(elbow_y), int(hand_x), int(hand_y))

        # Hand
        painter.setBrush(skin_color)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(int(hand_x - 5), int(hand_y - 5), 10, 10)

        # Fingers hint
        if self.hovering and not is_back:
            painter.setPen(QPen(skin_color.darker(110), 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap))
            for i in range(4):
                angle = -0.3 + i * 0.2
                fx = hand_x + math.cos(angle) * 8
                fy = hand_y - 8 + math.sin(angle) * 3
                painter.drawLine(int(hand_x), int(hand_y - 3), int(fx), int(fy))

    def draw_sparkles(self, painter, cx, cy):
        """Draw sparkle effect."""
        painter.setPen(QPen(QColor(255, 220, 100), 2))
        for i in range(8):
            angle = i * math.pi / 4 + self.walk_cycle
            inner = 20
            outer = 30
            x1 = cx + math.cos(angle) * inner
            y1 = cy + math.sin(angle) * inner
            x2 = cx + math.cos(angle) * outer
            y2 = cy + math.sin(angle) * outer
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))

        # Small stars
        painter.setBrush(QColor(255, 255, 200))
        painter.setPen(Qt.PenStyle.NoPen)
        for i in range(5):
            angle = i * math.pi * 2 / 5 + self.breath_cycle
            sx = cx + math.cos(angle) * 35
            sy = cy + math.sin(angle) * 25
            painter.drawEllipse(int(sx - 2), int(sy - 2), 4, 4)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.open_claude_terminal()
        elif event.button() == Qt.MouseButton.RightButton:
            QApplication.quit()

    def open_claude_terminal(self):
        self.clicked = True
        self.walking = False
        self.update()

        script = '''
        tell application "Terminal"
            activate
            do script "claude"
        end tell
        '''

        try:
            subprocess.run(["osascript", "-e", script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to open terminal: {e}")

        QTimer.singleShot(2000, self.resume_normal)

    def resume_normal(self):
        self.clicked = False
        self.walking = True

    def enterEvent(self, event):
        self.hovering = True

    def leaveEvent(self, event):
        self.hovering = False


def main():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)

    buddy = ClaudeBuddy()
    buddy.show()

    print("Claude Buddy is running!")
    print("  Left-click  → Open Claude in Terminal")
    print("  Right-click → Quit")

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
