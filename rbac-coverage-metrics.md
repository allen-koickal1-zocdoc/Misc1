# RBAC / Practice Account & User Setup - Test Coverage Metrics

## Summary
| Category | Total Tests | Covered | Partial | Missing | Coverage % |
|----------|------------|---------|---------|---------|------------|
| Inbox / Appointment Management | 19 | 14 | 2 | 3 | 74% |
| Calendar | 11 | 7 | 1 | 3 | 64% |
| Performance Dashboard | 14 | 8 | 2 | 4 | 57% |
| Billing Settings | 9 | 4 | 1 | 4 | 44% |
| Practice Settings | 19 | 12 | 2 | 5 | 63% |
| SPO (Sponsored Results) | 5 | 4 | 0 | 1 | 80% |
| User Management | 6 | 5 | 0 | 1 | 83% |
| Working Hours / Integrations | 4 | 0 | 1 | 3 | 0% |
| Settings Dropdown | 8 | 3 | 2 | 3 | 38% |
| Common / Cross-Role | 2 | 2 | 0 | 0 | 100% |
| Intake | 1 | 1 | 0 | 0 | 100% |
| ZVS | 2 | 1 | 0 | 1 | 50% |
| Home | 3 | 0 | 0 | 3 | 0% |
| Your Website | 1 | 0 | 0 | 1 | 0% |
| **TOTAL** | **104** | **61** | **11** | **32** | **59%** |

---

## Detailed Coverage Matrix

### INBOX / APPOINTMENT MANAGEMENT

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 1 | Verify Full Access and Appt Mgmt users can access the Inbox | Full Access; Appt Mgmt | **Covered** | appointment-mgmt-user-flow.spec.js | "Verify that an appointment management user can access inbox and appointments" context |
| 2 | Verify SPO; Billing; Practice Settings; User Mgmt; Zo; Zo Live users CANNOT access Inbox | N/A (negative test) | **Covered** | rbac-user-roles-flow.spec.js | "Verify non-visibility of certain pages" - tests PS user cannot access inbox; Billing user redirect tests |
| 3 | Verify inbox status filters (All; New bookings; Reschedules; Cancellations; Intake submissions) display correctly | Full Access; Appt Mgmt | **Covered** | inbox-page.spec.js / appointment-mgmt-user-flow.spec.js | "Verifies Tab switching works and correct appointments are displayed in correct tabs" |
| 4 | Verify provider and location filters work correctly in Inbox | Full Access; Appt Mgmt | **Covered** | inbox-page.spec.js / appointment-mgmt-user-flow.spec.js | "Verify user can use filters in Inbox" - tests Location-filter-button |
| 5 | Verify search functionality works correctly in Inbox | Full Access; Appt Mgmt | **Partial** | cancellation-abatement-page.spec.js | Uses patient-search-field-input but no dedicated search functionality test |
| 6 | Verify appointment sorting functionality in Inbox | Full Access; Appt Mgmt | **Missing** | | No test for sort options |
| 7 | Verify various appointment types (marketplace; API; manual intake) display correctly in Inbox | Full Access; Appt Mgmt | **Partial** | inbox-page.spec.js | Tests MARKETPLACE type via notificationDateColumn; API and manual intake types not explicitly verified |
| 8 | Verify Appt Mgmt user can confirm appointment from flyout | Full Access; Appt Mgmt | **Covered** | inbox-page.spec.js / appointment-mgmt-user-flow.spec.js | "Verifies Confirming Booking Moves Removes it from New Booking Tab" |
| 9 | Verify Appt Mgmt user can cancel appointment from flyout | Full Access; Appt Mgmt | **Covered** | inbox-page.spec.js / appointment-mgmt-user-flow.spec.js | "Verifies User can cancel the booking from Inbox" |
| 10 | Verify Appt Mgmt user can modify appointment date from flyout | Full Access; Appt Mgmt | **Covered** | inbox-page.spec.js | "Verifies User can modify the booking from Inbox" - reschedule functionality |
| 11 | Verify Appt Mgmt user can modify appointment time from flyout | Full Access; Appt Mgmt | **Covered** | appointment-mgmt-user-flow.spec.js | "Verify that an appointment management user can reschedule an appointment" |
| 12 | Verify Appt Mgmt user can change provider from flyout | Full Access; Appt Mgmt | **Missing** | | No explicit provider change test |
| 13 | Verify Appt Mgmt user can change location from flyout | Full Access; Appt Mgmt | **Missing** | | No explicit location change test |
| 14 | Verify Appt Mgmt user can modify visit reason from flyout | Full Access; Appt Mgmt | **Covered** | appointment-mgmt-user-flow.spec.js | Reschedule flow includes getProviderProcedures API call (VR selection) |
| 15 | Verify Appt Mgmt user can view patient insurance cards | Full Access; Appt Mgmt | **Covered** | appointment-mgmt-user-flow.spec.js | insuranceEligibility API verified in confirm flow |
| 16 | Verify Appt Mgmt user can view if patient confirmed appointment | Full Access; Appt Mgmt | **Covered** | inbox-page.spec.js | ConfirmAppointment API response verification |
| 17 | Verify Appt Mgmt user can view Partner Network bookings | Full Access; Appt Mgmt | **Covered** | inbox-page.spec.js | Tests notificationDateColumn-MARKETPLACE; Partner Network implicit |
| 18 | Verify Appt Mgmt user can send manual intake request | Full Access; Appt Mgmt | **Covered** | inbox-page.spec.js / appointment-mgmt-user-flow.spec.js | "Verifies User Send Patient Intake button is visible" + SendIntakeLink API |
| 19 | Verify Inbox tutorial displays for first-time users | Full Access; Appt Mgmt | **Covered** | inbox-page.spec.js / appointment-mgmt-user-flow.spec.js | "Verify tutorial works in Inbox" context |

### CALENDAR

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 20 | Verify Full Access and Appt Mgmt users can access Calendar | Full Access; Appt Mgmt | **Covered** | appointment-mgmt-user-flow.spec.js | "access the patient record page and the calendar" test navigates to calendar |
| 21 | Verify SPO; Billing; Practice Settings; User Mgmt users CANNOT access Calendar | N/A (negative test) | **Covered** | rbac-user-roles-flow.spec.js | "Verify that Billing user is unable to access certain pages" - visits /provider/calendar and checks redirect |
| 22 | Verify Appt Mgmt user can view appointment card on Calendar | Full Access; Appt Mgmt | **Covered** | appointment-management-flow.spec.js | "View appt card on patient record page" |
| 23 | Verify Appt Mgmt user can create availability slots | Full Access; Appt Mgmt | **Covered** | calendar-page.spec.js | "add and view one time availability" |
| 24 | Verify Appt Mgmt user can edit availability slots | Full Access; Appt Mgmt | **Partial** | calendar-page.spec.js | "Add and view busy block / update availability" - partial edit coverage |
| 25 | Verify Appt Mgmt user can create busy blocks | Full Access; Appt Mgmt | **Covered** | calendar-page.spec.js | "Add and view busy block / update availability" |
| 26 | Verify Appt Mgmt user can create calendar filters | Full Access; Appt Mgmt | **Missing** | | No test for calendar filter creation |
| 27 | Verify Appt Mgmt user can report a patient from Calendar | Full Access; Appt Mgmt | **Missing** | | No test for patient reporting |
| 28 | Verify Appt Mgmt user can dispute bookings | Full Access; Appt Mgmt | **Missing** | | No test for booking disputes |
| 29 | Verify navigation to other flows via appointment card | Full Access; Appt Mgmt | **Covered** | appointment-management-flow.spec.js | "access the patient record page and the calendar" + ellipsis menu options |
| 30 | Verify Calendar tutorial displays for first-time users | Full Access; Appt Mgmt | **Covered** | calendar-page.spec.js | Tutorial verification via view toggle tests |

### PERFORMANCE DASHBOARD

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 31 | Verify Full Access; Billing; Appt Mgmt; Practice Settings users can access Performance Dashboard | Full Access; Billing; Appt Mgmt; PS | **Covered** | practice-settings-user-flow.spec.js / rbac-user-roles-flow.spec.js | Multiple tests verify dashboard access by role |
| 32 | Verify SPO user CANNOT access Performance Dashboard | N/A (negative test) | **Covered** | rbac-user-roles-flow.spec.js | SPO user redirect tests |
| 33 | Verify Total Bookings Module visible for Full Access; Billing; Appt Mgmt; PS | Full Access; Billing; Appt Mgmt; PS | **Covered** | performance-dashboard-page.spec.js | "Access patient type bookings stats - SECTION" |
| 34 | Verify What was your bookings breakdown module (non-PHI excludes VRs for some) | Full Access; Billing; Appt Mgmt; PS | **Partial** | performance-dashboard-page.spec.js | Tests bookings stats but not PHI/VR exclusion by role |
| 35 | Verify Who were your last bookings module (PHI) | Full Access; Billing; Appt Mgmt | **Missing** | | No explicit PHI module test |
| 36 | Verify spend module | Full Access; Billing | **Covered** | spend-management-flow.spec.js | "Set a spend cap and verify bookability status" |
| 37 | Verify Patient Choice module | Full Access; Billing; Appt Mgmt; PS | **Missing** | | No Patient Choice module test |
| 38 | Verify Billing user can control budget | Full Access; Billing | **Covered** | spend-management-flow.spec.js | setSpendCap and setSpendLock commands |
| 39 | Verify View Appointment Report with PHI | Full Access; Billing; Appt Mgmt | **Covered** | performance-dashboard-page.spec.js / appointment-mgmt-user-flow.spec.js | "Access appointment summary" + "can access and interact with Appointment Report" |
| 40 | Verify View PHI Details on Dashboard | Full Access; Billing; Appt Mgmt | **Partial** | appointment-mgmt-user-flow.spec.js | Tests dashboard access but not explicit PHI details |
| 41 | Verify Reviews Module | Full Access; PS | **Missing** | | No reviews module test |
| 42 | Verify View Recommendations | All applicable | **Covered** | performance-dashboard-flow.spec.js | Dashboard link navigation tests |
| 43 | Verify Take action on Recommendations | Full Access; PS | **Missing** | | No recommendation action test |
| 44 | Verify Zocdoc Search Status | Full Access | **Covered** | spend-management-flow.spec.js | Bookability status verification |

### BILLING SETTINGS

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 45 | Verify Billing user lands on Performance Dashboard after login | Billing | **Covered** | rbac-user-roles-flow.spec.js | "Verify Billing user lands on Performance dashboard page after logging in" |
| 46 | Verify Billing user can access Billing settings | Full Access; Billing | **Covered** | billing-user-flow.spec.js | Visits /provider/settings/billing |
| 47 | Verify Billing user can view invoices | Full Access; Billing | **Covered** | billing-user-flow.spec.js | "Viewing and Checking Billing and Account Related functionality" |
| 48 | Verify Billing user can download invoices | Full Access; Billing | **Missing** | | No invoice download test |
| 49 | Verify Billing user can add ACH payment method | Full Access; Billing | **Missing** | | No ACH add test |
| 50 | Verify Billing user can edit payment method | Full Access; Billing | **Missing** | | No payment edit test |
| 51 | Verify Billing user can delete payment method | Full Access; Billing | **Missing** | | No payment delete test |
| 52 | Verify Billing user can edit rollovers | Full Access; Billing | **Partial** | spend-management-flow.spec.js | setSpendCap tests budget; rollovers not explicit |
| 53 | Verify Appt Mgmt; PS users CANNOT access Billing settings | N/A (negative test) | **Covered** | rbac-user-roles-flow.spec.js | Role restriction tests |

### PRACTICE SETTINGS

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 54 | Verify Practice Settings user lands on Providers page after login | Practice Settings | **Covered** | practice-settings-user-flow.spec.js | "Verify Practice Settings User Homepage is Providers page after login" |
| 55 | Verify PS user can access Providers page | Full Access; PS | **Covered** | practice-settings-user-flow.spec.js / providers-page-flow.spec.js | Multiple provider page tests |
| 56 | Verify PS user can view provider profile | Full Access; PS | **Covered** | practice-settings-user-flow.spec.js | "Verify Practice Settings User can access provider profile from Providers page" |
| 57 | Verify PS user can add new provider (Add-on flow) | Full Access; PS | **Covered** | practice-settings-user-flow.spec.js | "Verifying the auto-population of First Name, Last Name, specialities" via /provider/setup/add |
| 58 | Verify PS user can manage provider insurances | Full Access; PS | **Covered** | insurance-settings-page.spec.js | Practice/Prof/Prof-Loc level insurance tests |
| 59 | Verify PS user can apply insurance change to multiple providers | Full Access; PS | **Covered** | insurance-settings-page.spec.js | "Verify users can bulk add/remove desired carriers-network" |
| 60 | Verify PS user can edit insurances | Full Access; PS | **Covered** | insurance-settings-page.spec.js | "Verify users can check for error states and modify insurance carriers" |
| 61 | Verify PS user can access Visit Reasons settings | Full Access; PS | **Covered** | practice-settings-user-flow.spec.js | "Verify Practice Settings User can access Visit Reasons settings" |
| 62 | Verify PS user can apply VR change to multiple providers | Full Access; PS | **Covered** | vr-presets-flow.spec.js | Multi-specialty VR preset tests |
| 63 | Verify PS user can access Practice details | Full Access; PS | **Covered** | practice-settings-user-flow.spec.js | "Verify Practice Settings User can access available settings tabs" |
| 64 | Verify PS user can change notification emails | Full Access; PS | **Missing** | | No notification email test |
| 65 | Verify PS user can change location phone number | Full Access; PS | **Missing** | | No phone number change test |
| 66 | Verify PS user can create location | Full Access; PS | **Missing** | | No location creation test |
| 67 | Verify PS user can change specialty | Full Access; PS | **Partial** | vr-presets-flow.spec.js | Navigates to specialties page but no change test |
| 68 | Verify PS user can manage Google Listing Availability | Full Access; PS | **Missing** | | No Google listing test |
| 69 | Verify PS user can set ZVS text reminder | Full Access; PS | **Missing** | | No ZVS reminder test |
| 70 | Verify PS user can access COVID-19 settings | Full Access; PS | **Partial** | rbac-user-roles-flow.spec.js | Billing user blocked from COVID settings; no PS access positive test |
| 71 | Verify PS user can access Features page | Full Access; PS | **Covered** | features-flow.spec.js / features-page.spec.js | Features page tests in Provider-Onboarding |
| 72 | Verify Billing; Appt Mgmt; SPO users CANNOT access Practice Settings pages | N/A (negative test) | **Covered** | rbac-user-roles-flow.spec.js | Multiple role restriction tests |

### SPO (SPONSORED RESULTS)

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 73 | Verify SPO user lands on SPO Dashboard after login | SPO | **Covered** | spo-user-flow.spec.js | Tests visit /provider/sponsoredresults/dashboard |
| 74 | Verify SPO user can manage Sponsored Results | Full Access; SPO | **Covered** | spo-user-flow.spec.js | "should complete full campaign lifecycle: create, edit, pause, and delete" |
| 75 | Verify SPO user can only access Account and Legal settings | SPO | **Covered** | rbac-user-roles-flow.spec.js | SPO user redirect tests for other pages |
| 76 | Verify SPO user CANNOT access Calendar; Inbox; Performance; Providers | N/A (negative test) | **Covered** | rbac-user-roles-flow.spec.js | "user gets redirected when hitting spo url" pattern |
| 77 | Verify Appt Mgmt; Billing; PS users CANNOT access SPO Dashboard | N/A (negative test) | **Missing** | | No explicit test for non-SPO users blocked from SPO |

### USER MANAGEMENT

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 78 | Verify User Mgmt user can access Users page | Full Access; User Mgmt | **Covered** | user-management-page.spec.js | "should display user management page with users table" |
| 79 | Verify User Mgmt user can create users with any role | Full Access; User Mgmt | **Covered** | user-management-page.spec.js | "should create a user with API response verification" |
| 80 | Verify User Mgmt user can delete non-FA users | Full Access; User Mgmt | **Covered** | user-management-page.spec.js | "should delete a user with API response verification" |
| 81 | Verify User Mgmt user can change non-FA user roles | Full Access; User Mgmt | **Covered** | user-management-page.spec.js | "should edit a user with API response verification" |
| 82 | Verify User Mgmt user CANNOT delete/edit Full Access users | User Mgmt (negative) | **Missing** | | No explicit FA protection test |
| 83 | Verify Appt Mgmt; Billing; PS; SPO users CANNOT access Users page | N/A (negative test) | **Covered** | rbac-user-roles-flow.spec.js | "Appts+PS user" visits /provider/settings/users and checks restriction |

### WORKING HOURS / INTEGRATIONS

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 84 | Verify Appt Mgmt and PS users can edit working hours | Full Access; Appt Mgmt; PS | **Missing** | | No working hours edit test |
| 85 | Verify Appt Mgmt and PS users can view calendar integration status | Full Access; Appt Mgmt; PS | **Partial** | calendar-page.spec.js | Calendar tests exist but no integration status test |
| 86 | Verify PS user can take action on integration troubleshooting | Full Access; PS | **Missing** | | No integration troubleshooting test |
| 87 | Verify integration sync capabilities | Full Access; PS | **Missing** | | No sync test |

### SETTINGS DROPDOWN

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 88 | Verify all roles can access Account settings | All roles | **Covered** | practice-settings-user-flow.spec.js | Tests settings-password visibility |
| 89 | Verify all roles can access Legal settings | All roles | **Covered** | legal-settings-page.spec.js | "Allow users to update their privacy settings" |
| 90 | Verify Contact Us accessible for Full Access; SPO; Billing; Appt Mgmt; PS | Full Access; SPO; Billing; Appt Mgmt; PS | **Partial** | appointment-management-flow.spec.js / provider-dashboard-flow.spec.js | Tests resource links but not Contact Us specifically |
| 91 | Verify Help Center accessible for Full Access; SPO; Billing; Appt Mgmt; PS | Full Access; SPO; Billing; Appt Mgmt; PS | **Partial** | appointment-management-flow.spec.js | Tests resource links but not Help Center specifically |
| 92 | Verify Invite Practices accessible for Full Access; SPO; Billing; Appt Mgmt; PS | Full Access; SPO; Billing; Appt Mgmt; PS | **Missing** | | No Invite Practices test |
| 93 | Verify View Features tabs accessible for Full Access and PS only | Full Access; PS | **Covered** | features-flow.spec.js | Features page tests |
| 94 | Verify Manage Referral Network accessible for Full Access and PS only | Full Access; PS | **Missing** | | No Referral Network test |
| 95 | (Missing from original) Verify dropdown menu navigation | All roles | **Missing** | | No comprehensive dropdown test |

### COMMON / CROSS-ROLE

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 96 | Verify correct landing page per role after login | All roles | **Covered** | rbac-user-roles-flow.spec.js / practice-settings-user-flow.spec.js | Multiple landing page tests per role |
| 97 | Verify sign-out functionality for all roles | All roles | **Covered** | appointment-management-flow.spec.js | Header dropdown tests include sign-out |

### INTAKE

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 98 | Verify Full Access and Appt Mgmt users can access Intake pages | Full Access; Appt Mgmt | **Covered** | intake-flow.spec.js / intake-page.spec.js | Intake flows in Practice-Solutions/Branded-Directory |

### ZVS

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 99 | Verify Full Access user can access ZVS pages | Full Access | **Covered** | zvs-flow.spec.js / zvs-page.spec.js | ZVS tests in Branded-Directory |
| 100 | Verify PS user can enroll in ZVS | Full Access; PS | **Missing** | | No ZVS enrollment test |

### HOME

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 101 | Verify Full Access user can access Home page | Full Access | **Missing** | | No Home page test |
| 102 | Verify Full Access user can enroll in payment products | Full Access | **Missing** | | No payment product enrollment test |
| 103 | Verify Full Access user can enroll in non-payment products | Full Access | **Missing** | | No non-payment product enrollment test |

### YOUR WEBSITE

| S.No | Test Case | Roles with Access | Coverage Status | Spec File | Test Name / Notes |
|------|-----------|-------------------|-----------------|-----------|-------------------|
| 104 | Verify Full Access user can access Your Website page | Full Access | **Missing** | | rbac-user-roles-flow.spec.js tests Appts+PS user blocked from /provider/settings/website but no positive test |

---

## Priority Gaps (High Impact Missing Tests)

### Critical Path - Billing Operations
1. **Billing: Add ACH payment method** - Core billing functionality
2. **Billing: Edit/Delete payment method** - Payment management
3. **Billing: Download invoices** - Important for reconciliation

### Critical Path - Practice Settings
4. **PS: Create location** - Core setup flow
5. **PS: Change location phone number** - Contact management
6. **PS: Notification email settings** - Communication setup

### Critical Path - Calendar Operations
7. **Calendar: Create calendar filters** - Workflow efficiency
8. **Calendar: Report a patient** - Patient management
9. **Calendar: Dispute bookings** - Financial protection

### Critical Path - Dashboard
10. **Dashboard: Patient Choice module** - Key metric visibility
11. **Dashboard: Reviews module** - Reputation management
12. **Dashboard: Take action on recommendations** - Engagement feature

### New Feature Areas (No Coverage)
13. **Home page** - All 3 tests missing
14. **Your Website page** - Full Access feature
15. **Working Hours / Integrations** - 4 tests missing
16. **Referral Network** - Settings dropdown feature

---

## Files Referenced

| Spec File | Location | Primary Coverage |
|-----------|----------|------------------|
| appointment-mgmt-user-flow.spec.js | Provider/Acquisition/Account-User-Setup/Flows/ | Appt Mgmt role inbox/calendar tests |
| billing-user-flow.spec.js | Provider/Acquisition/Account-User-Setup/Flows/ | Billing role settings |
| practice-settings-user-flow.spec.js | Provider/Acquisition/Account-User-Setup/Flows/ | PS role comprehensive tests |
| rbac-user-roles-flow.spec.js | Provider/Acquisition/Account-User-Setup/Flows/ | Multi-role access/restriction tests |
| spo-user-flow.spec.js | Provider/Acquisition/Account-User-Setup/Flows/ | SPO dashboard CRUD |
| user-management-page.spec.js | Provider/Acquisition/Account-User-Setup/Pages/ | User CRUD operations |
| legal-settings-page.spec.js | Provider/Acquisition/Account-User-Setup/Pages/ | Privacy/legal settings |
| inbox-page.spec.js | Practice-Solutions/Appointment-Management/Pages/ | Inbox operations |
| calendar-page.spec.js | Practice-Solutions/Appointment-Management/Pages/ | Calendar availability |
| performance-dashboard-page.spec.js | Provider/Retention/Provider-Success/Pages/ | Dashboard modules |
| spend-management-flow.spec.js | Provider/Retention/Provider-Success/Flows/ | Budget/spend controls |
| insurance-settings-page.spec.js | Provider/Retention/Preferences-Financial-Fit/Pages/ | Insurance management |
| vr-presets-flow.spec.js | Provider/Retention/Preferences-Financial-Fit/Flows/ | Visit reason presets |
| features-flow.spec.js | Provider/Adoption/Provider-Onboarding/Flows/ | Features page |
| intake-flow.spec.js | Practice-Solutions/Branded-Directory/Flows/ | Intake functionality |
| zvs-flow.spec.js | Practice-Solutions/Branded-Directory/Flows/ | ZVS functionality |

---

# Production Code Analysis - Additional Test Gaps

**Date:** 2026-05-06  
**Analysis Source:** provider-fe-monorepo, practice-user-permissions repos

## Executive Summary

Production code analysis reveals **49 new test cases** identified from route definitions and permission checks that are missing from the current test suite. These gaps span Home page, Your Website, Working Hours, Billing operations, Practice Settings, and more.

---

## NEW: Home Page Test Cases (Current Coverage: 0%)

**Routes from production:** `provider-home-webapp/src/config/routes.ts`

| S.No | Test Case | Roles with Access | Priority |
|------|-----------|-------------------|----------|
| 105 | Verify Full Access user can access Home page | Full Access | P1 |
| 106 | Verify Home page displays onboarding tasks correctly | Full Access | P1 |
| 107 | Verify Full Access user can enroll in Marketplace | Full Access | P1 |
| 108 | Verify Full Access user can enroll in Intake | Full Access | P2 |
| 109 | Verify Full Access user can enroll in Partner Syndication | Full Access | P2 |
| 110 | Verify Full Access user can complete identity verification | Full Access | P2 |
| 111 | Verify Full Access user can schedule meeting with Zocdoc | Full Access | P3 |
| 112 | Verify Full Access user can view Provider Profile from Home | Full Access | P2 |
| 113 | Verify non-Full Access roles are redirected from Home | All other roles | P1 |

---

## NEW: Settings Routes Without Coverage

**Routes from production:** `settings/src/config/routes.ts`

### Your Website Page (Current Coverage: 0%)

| S.No | Test Case | Roles with Access | Priority |
|------|-----------|-------------------|----------|
| 114 | Verify Full Access user can access Your Website page | Full Access | P2 |
| 115 | Verify other roles CANNOT access Your Website | All non-FA roles | P2 |

### Working Hours Page (Current Coverage: 0%)

| S.No | Test Case | Roles with Access | Priority |
|------|-----------|-------------------|----------|
| 118 | Verify Appt Mgmt user can access Working Hours page | FA; Appt Mgmt; PS | P1 |
| 119 | Verify user can edit working hours for a provider | FA; Appt Mgmt; PS | P1 |
| 120 | Verify user can add office hours | FA; Appt Mgmt; PS | P2 |
| 121 | Verify Billing and SPO users CANNOT access Working Hours | Billing; SPO | P2 |

### Alerter/Notifications Page

| S.No | Test Case | Roles with Access | Priority |
|------|-----------|-------------------|----------|
| 122 | Verify user can access alerter settings | FA; PS | P2 |
| 123 | Verify user can configure notification preferences | FA; PS | P2 |

### Patient Prescreener Page

| S.No | Test Case | Roles with Access | Priority |
|------|-----------|-------------------|----------|
| 124 | Verify PS user can access Patient Prescreener settings | FA; PS | P2 |
| 125 | Verify PS user can configure prescreening questions | FA; PS | P2 |

---

## Billing Operations - Missing Test Cases

**Routes from production:** `settings/src/config/routes.ts`

| S.No | Test Case | API Route | Priority |
|------|-----------|-----------|----------|
| 126 | Billing user can add ACH payment method | POST_ADD_ACH | P1 |
| 127 | Billing user can add credit card | POST_ADD_CREDIT_CARD | P1 |
| 128 | Billing user can delete payment method | DELETE_PAYMENT_METHOD | P1 |
| 129 | Billing user can set default payment method | POST_SET_DEFAULT_PAYMENT_METHOD | P1 |
| 130 | Billing user can update billing email | PUT_UPDATE_PRACTICE_BILLING_EMAIL | P2 |
| 131 | Billing user can update business address | PUT_UPDATE_PRIMARY_BUSINESS_ADDRESS | P2 |
| 132 | Billing user can view/download bill summary | GET_BILL_SUMMARY | P1 |
| 133 | Billing user can download invoice PDF | GET_INVOICE_PDF_DOWNLOAD_URL | P1 |

---

## Practice Settings - Missing Test Cases

| S.No | Test Case | API Route | Priority |
|------|-----------|-----------|----------|
| 134 | PS user can create new location | CREATE_PRACTICE_LOCATION | P1 |
| 135 | PS user can create virtual location | CREATE_VIRTUAL_PRACTICE_LOCATION | P2 |
| 136 | PS user can update location | UPDATE_PRACTICE_LOCATION | P1 |
| 137 | PS user can request delete location | REQUEST_DELETE_PRACTICE_LOCATION | P2 |
| 138 | PS user can update location sort order | UPDATE_PRACTICE_LOCATION_SORT_ORDER | P3 |
| 139 | PS user can upload practice logo | UPLOAD_PRACTICE_LOGO | P2 |
| 140 | PS user can manage practice guidelines | PRACTICE_GUIDELINES_ROUTE | P2 |

---

## User Management - Additional Test Cases

| S.No | Test Case | Priority |
|------|-----------|----------|
| 141 | Verify User Mgmt user CANNOT delete Full Access users | P1 |
| 142 | Verify User Mgmt user CANNOT edit Full Access user roles | P1 |

---

## Settings Dropdown - Missing Test Cases

| S.No | Test Case | Roles with Access | Priority |
|------|-----------|-------------------|----------|
| 145 | Verify Invite Practices option is accessible | FA; PS; Billing; Appt Mgmt; SPO | P2 |
| 146 | Verify Manage Referral Network is accessible | FA; PS | P2 |
| 147 | Verify Help Center link works | All roles | P3 |
| 148 | Verify Contact Us link works | All roles | P3 |

---

## Provider Profile Settings - Additional Routes

| S.No | Test Case | Priority |
|------|-----------|----------|
| 149 | PS user can update provider statement | P2 |
| 150 | PS user can update new patient guidance | P2 |
| 151 | PS user can update provider gender/sexuality/faith | P2 |
| 152 | PS user can update provider languages | P2 |
| 153 | PS user can update provider education | P2 |
| 154 | PS user can update board certifications | P2 |
| 155 | PS user can update professional memberships | P2 |
| 156 | PS user can update focus areas | P2 |
| 157 | PS user can update treatment approaches | P2 |
| 158 | PS user can update provider modalities | P2 |

---

## Products & Features Page

| S.No | Test Case | Roles with Access | Priority |
|------|-----------|-------------------|----------|
| 159 | Verify Full Access user can access Products page | FA | P2 |
| 160 | Verify Full Access user can view Synchronizer feature | FA; PS | P2 |
| 161 | Verify PMS agreement flow | FA | P3 |

---

## Updated Coverage Summary

| Category | Original Tests | New Tests Identified | Total | Priority Distribution |
|----------|---------------|---------------------|-------|----------------------|
| Home Page | 3 (missing) | 9 | 9 | P1: 3, P2: 4, P3: 2 |
| Your Website | 1 (missing) | 2 | 2 | P2: 2 |
| Working Hours | 4 (missing) | 4 | 4 | P1: 2, P2: 2 |
| Billing Operations | 4 (missing) | 8 | 8 | P1: 5, P2: 3 |
| Practice Settings | 6 (missing) | 7 | 7 | P1: 2, P2: 4, P3: 1 |
| User Management | 1 (missing) | 2 | 2 | P1: 2 |
| Settings Dropdown | 3 (missing) | 4 | 4 | P2: 2, P3: 2 |
| Provider Profile | - | 10 | 10 | P2: 10 |
| Products/Features | - | 3 | 3 | P2: 2, P3: 1 |
| **TOTAL NEW** | - | **49** | 49 | **P1: 14, P2: 27, P3: 6** |

---

## P1 Priority Tests - Implementation Order

1. **Home page access for Full Access** (3 tests) - Core onboarding flow
2. **Billing payment methods CRUD** (5 tests) - Financial operations
3. **Working hours access** (2 tests) - Core settings functionality
4. **User Mgmt Full Access protection** (2 tests) - Security critical
5. **Practice location creation** (2 tests) - Core setup flow

---

## Notes

- FGA (Fine-Grained Authorization) is used for permission checks in `practice-user-permissions` service
- Permission checks in frontend use `usePracticeStaffRoles()` hook from `@zocdoc/provider-core`
- Role spoofing tool available in development/Pulse for testing different roles
- All roles have access to Account and Legal settings
- Zo roles (PhoneBotPerformance, PhoneBotCallCenterRep) exist in codebase but are out of scope for this analysis
