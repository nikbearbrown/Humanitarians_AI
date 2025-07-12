# Kanban Board – Phase 3 Requirements

**Last Updated:** November 18, 2024  
**Source:** Post Phase 2 Demo Review with Prof. Nik Bear Brown

## Overview

This document outlines the scope of **Phase 3** enhancements and functional requirements for the **Kanban Board Project**. These changes follow the feedback received during the Phase 2 demo meeting. The primary focus is on improving project visibility for executive stakeholders, refining user interface elements, and integrating updated project and volunteer data.

---

## Requirements from Prof. Nik Bear Brown

1. **Company-Wide Project Visibility**
   - Display a comprehensive list of all existing projects in the organization.
   - Include clear, concise descriptions for each project in the list.

2. **Project Activity Tracking**
   - Indicate which projects are currently active vs inactive.
   - Show the current status of each active project (e.g., In Progress, Completed, On Hold).

3. **Source Code Access**
   - Provide clickable GitHub repository links for each project.
   - Specify the cloud hosting location (AWS, GCP, etc.) if applicable.

4. **CEO Dashboard Functionality**
   - When a user logs in with the **CEO role**, they should see:
     - All company projects
     - Their current statuses (Active/Inactive)
     - Assigned team members
     - Hosting and repository details

5. **Search Functionality**
   - Implement a **search bar** for users to search projects and volunteers dynamically from the admin/CEO interface.

6. **Volunteer-Project Mapping**
   - Clearly show which volunteers are working on which projects.
   - Ensure this information is viewable from both the Admin and CEO dashboards.

7. **Project Metadata Update**
   - Update all project details based on information provided by **Raghyna**.

---

## Frontend Team – Ideation & UI Requirements

1. **New Admin Page Design**
   - A redesigned admin interface to accommodate the updated feature set.
   - Should support easier navigation, project insights, and volunteer management.

2. **Software Tour Integration**
   - Incorporate a **software walkthrough** or onboarding tour to help new users (especially admins) understand system usage and functionalities.

3. **People Page Enhancement**
   - List all current volunteers with their:
     - Name
     - Role
     - Assigned Projects
     - Contact Email

---

## Suggested Structure

```

kanban-board/
├── backend/
│   └── apis/
│       ├── projects.js        # Project metadata, status, GitHub links
│       ├── volunteers.js      # Volunteer-project mapping
│       └── auth.js            # Role-based access (e.g., CEO, Admin)
├── frontend/
│   └── components/
│       ├── AdminDashboard/
│       ├── CEODashboard/
│       ├── ProjectSearchBar/
│       └── PeoplePage/
├── public/
│   └── software-tour/         # Files for the guided tour
└── README.md

```

---

## 📎 Resources and References

- [Kanban Project Repository](https://github.com/Humanitariansai/kanban-board-frontend)
- [Figma Design File](https://www.figma.com/board/mxMNKcci5hSlNWAdd406BF/OPT-Portal-and-Kanban-Board-Project?node-id=0-1)
- [Admin Flow (Demo Link)](https://drive.google.com/file/d/11V6_qcCGawr_gjUxdIlEBIRHR-y_nXRR/view?usp=sharing)
- [PM Flow](https://drive.google.com/file/d/1rJV1LTtE3YtE-9_lFYp2PBUNeo7lhZj-/view?usp=sharing)
- [Volunteer Flow](https://drive.google.com/file/d/1Q74YC5Rq5NJnia4a2-Jar5dXQ7q-Jm1-/view?usp=sharing)

---

## 🧑‍💼 Maintainers

- **Technical Project Manager**: Rahul Ashok Kodate (kodate.rahulashok@humanitarians.ai)
- **Frontend Lead**: Pranjal Sharma
- **Advisor**: Prof. Nik Bear Brown

---

## 📅 Timeline

Phase 3 development and review to be completed by **December 2024**, with weekly deliverables and demo reviews.

---

For questions, please contact the project maintainers or refer to the Figma/Google Drive resources above.
```
