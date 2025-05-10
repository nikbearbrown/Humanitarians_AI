# Kanban Board - Phase 1  
**OPT Volunteers Management System**  
**Timeline: August 4, 2024 – September 13, 2024**

---

## Phase Overview

Phase 1 involved the planning, development, and deployment of the Kanban Board application to manage volunteers associated with the OPT Portal project. The work was executed across 6 structured weeks, focusing on requirement gathering, backend and frontend setup, API design, testing, and deployment on Google Cloud Platform (GCP).

---

## Weekly Breakdown

### Week 1 (August 4 – August 9)  
**Stage 1: Planning and Design**

**Objectives:**
- Understand core application requirements
- Define technical and user requirements
- Develop initial design wireframes

**Tasks:**
- Define user roles: Admin, Project Manager, Volunteer
- Document functional and non-functional requirements
- Write user stories and use cases
- Design MongoDB schema (Users, Projects, Tasks, Comments, Notifications)
- Define API specifications with authentication methods
- Create wireframes/mockups for all user roles using Figma
- Draft Admin, Project Manager, and Volunteer dashboards

---

### Week 2 (August 12 – August 16)  
**Stage 2: Setup and Basic Implementation**

**Objectives:**
- Prepare the development and cloud environments
- Establish initial backend and frontend structures

**Tasks:**
- Set up Node.js and React environments
- Configure GCP: Compute Engine, Cloud Storage, Cloud SQL
- Initialize Git repositories and define branching strategy
- Configure CI/CD using Google Cloud Build
- Develop base backend with initial authentication and project endpoints
- Set up React frontend with routing, login, and dashboard components

---

### Week 3 (August 19 – August 23)  
**Stage 2 Continued: Backend and Frontend Development**

**Objectives:**
- Integrate MongoDB and continue API/backend development
- Develop key frontend components and connect them to backend

**Tasks:**
- Implement MongoDB connection and test CRUD operations
- Build backend APIs: user registration, login, and project creation
- Implement frontend login and dashboard functionality
- Integrate frontend and backend using API calls

---

### Week 4 (August 26 – August 30)  
**Stage 3: Core Development and Testing**

**Objectives:**
- Develop advanced features and establish secure user flow
- Conduct component-level testing and refinement

**Tasks:**
- Create task management APIs (create, update, delete)
- Build APIs for comments and notifications
- Implement business logic for assignments and progress tracking
- Develop task board, task detail, comments, and notifications components
- Set up JWT authentication and role-based access control (RBAC)

---

### Week 5 (September 2 – September 6)  
**Stage 3 Continued: Testing and Initial Deployment**

**Objectives:**
- Perform internal testing
- Deploy MVP on GCP

**Tasks:**
- Deploy backend and frontend on GCP with environment variables
- Conduct unit and integration testing
- Perform load testing for performance assessment
- Plan for secure communication and encryption practices

---

### Week 6 (September 9 – September 13)  
**Stage 4: Finalization and Launch**

**Objectives:**
- Final testing and optimization
- Launch MVP with documentation

**Tasks:**
- Implement HTTPS and secure APIs
- Encrypt sensitive user and project data
- Conduct user acceptance testing (UAT) with Admins, PMs, Volunteers
- Optimize frontend and backend performance
- Final deployment on GCP with scalability options
- Deliver user documentation and collect post-launch feedback

---

## Final Outcome

The Kanban Board Phase 1 was successfully completed with a fully functional minimum viable product (MVP) deployed on Google Cloud. It includes role-based dashboards, authentication, project/task management, and collaborative features. The system is now positioned for enhancement in future phases.
