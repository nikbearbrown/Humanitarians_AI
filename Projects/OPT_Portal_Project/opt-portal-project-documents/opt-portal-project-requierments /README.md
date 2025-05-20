# OPT Portal Project – Requirements

This repository contains the detailed requirements for the **OPT Portal Project**, specifically for **Phase 2 and Phase 3** of the project. The goal is to provide a comprehensive understanding of the functionality, workflow, and features to be implemented in the system.

---

## Phase 2 Requirements – Timesheet Module

### Team Members:
- Gayathri Vummenthala
- Rahul Ashok Kodate
- Saurav Shaw
- Rajas Telang
- Visrutha Abbaiah Reddy
- More TBD

### Introduction:
In **Phase 2**, the primary objective is to implement the **Timesheet module** within the OPT Portal. This feature will enable volunteers to efficiently log and update their weekly working hours. Below are the specific requirements for this module:

### 1. User Roles and Permissions:
- **User roles** need to be clearly defined, such as:
  - Volunteers
  - Project Managers/Mentors
  - System Administrators
- Define specific permissions for each role, such as viewing, submitting, approving, or rejecting timesheets.

### 2. Submission Deadlines and Reminders:
- Define the deadline for timesheet submissions (e.g., end of the week).
- Set up automated reminders for volunteers who have not submitted their timesheets.

### 3. Approval Workflow:
- Define the workflow for timesheet approval.
- Project Managers/Mentors must approve or reject timesheets within a specified time period.
- Implement automated escalation if timesheets are not approved within a set period (e.g., escalate to higher management).

### 4. Email Notifications:
- Customizable templates for email notifications.
- Notifications for warnings, ultimate warnings, and approval/rejection of timesheets.

### 5. Warning System:
- Track the number of warnings issued to each volunteer.
- Option to reset the warning count after a specified period or based on performance improvements.

### 6. Dashboard for Volunteers and Managers:
- Volunteers: Track submitted timesheets, approval status, and warnings.
- Managers: View and manage timesheets for their team, with sorting/filtering options based on approval status.

### 7. Reporting and Analytics:
- Generate reports on volunteers' working hours, approval rates, and warning counts.
- Weekly/monthly summaries for individuals and teams.

### 8. Data Export and Integration:
- Option for exporting timesheet data to formats like CSV.
- Integration with other systems such as HR or payroll systems.

### 9. Security and Audit Trail:
- Secure access to timesheet data.
- Implement an audit trail to track changes made to timesheets, including who approved, declined, or modified the hours.

---

## Phase 3 Requirements – Volunteer Management

After the **Phase 2 demo meeting**, the **Phase 3 requirements** will be implemented. These requirements include functionality for managing volunteer profiles and project details.

### Professor Nik Brown's Requirements:
1. **Profile page for each volunteer**:
   - Display all relevant volunteer information, such as:
     - Start and end dates
     - Project they are working on
     - Status (active/inactive)
   - A search bar to find volunteers using their **Volunteer ID**.

### OPT Team Ideation and Requirements:
1. **Role Management**:
   - **Super User**: Manually adds the first **Admin** role.
   - Admin can assign roles to other users (e.g., Admin/Project Manager, Project Manager, Volunteer).
   - **Project Manager** cannot assign roles.

2. **React State**:
   - A React state will be used to select user roles, allowing the Super User to assign roles to users.
  
3. **Software Tour**:
   - Integration with server APIs to allow the OPT Portal and Kanban Portal to interact.

4. **Database Setup**:
   - Set up the **OPT Portal database** on **AWS**.
   - Ensure the Kanban team can retrieve volunteer data from the database.

5. **Volunteer Details Page**:
   - Display details of volunteers, including the projects they are working on.

6. **Timesheet Error Resolution**:
   - Address timesheet errors and provide resolution processes.

7. **Application List**:
   - Implement an "Accept" or "Decline" button for application management.
   - Once an application is accepted, call the API to update it in the database and create the user.

---

## Conclusion

By implementing these phases, we aim to streamline volunteer management and timesheet tracking. These features will enhance transparency, accountability, and data accuracy, ensuring the project's success.

This repository serves as a living document, detailing the functional and technical requirements that will guide the development of the **OPT Portal** in the upcoming phases.

---

## Project Contributors

- **Project Manager**: Rahul Ashok Kodate  
- **Team Members**:
  - Gayathri Vummenthala
  - Saurav Shaw
  - Rajas Telang
  - Visrutha Abbaiah Reddy
  - Additional members TBD
