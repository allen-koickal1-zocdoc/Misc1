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
