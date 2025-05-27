# OPT Portal Project

## Abstract

The OPT Portal Project is a comprehensive web-based application designed to automate and streamline the Optional Practical Training (OPT) application process for international students and educational institutions. Functioning as a specialized hybrid of Jira and Monday.com tailored for OPT management, this full-stack solution addresses the administrative challenges by providing a centralized platform for document submission, application tracking, and status updates. The portal features dual interfaces: a student-facing system enabling document uploads and application monitoring, and an administrative dashboard for reviewing submissions and managing workflows similar to popular project management tools. Built using React.js for the frontend, Node.js and Express.js for the backend, and MongoDB for data storage, the application incorporates real-time notifications, secure document management, and role-based access control. The project is being developed by a structured team at Humanitarians.AI, with Rahul Ashok Kodate serving as the Technical Project Manager. The OPT Portal aims to enhance efficiency, transparency, and collaboration across university departments while providing international students with a self-service platform to navigate their OPT application journey through familiar project management interfaces.

## Project Overview

The **OPT Portal** is a full-stack web application developed to streamline and automate the management of Optional Practical Training (OPT) applications for international students. It enables users to track their application status, submit necessary documents, and receive notifications related to the OPT process. The portal is designed for educational institutions and international students and serves to simplify the administrative burden of managing OPT applications.

---

## Key Features

- **Student User Interface:**
  - Submit necessary OPT documents
  - Track the status of OPT application
  - Receive updates on application progress
  - Secure login and account management

- **Admin User Interface:**
  - Review student submissions
  - Update application status
  - Manage student workflows and communications

- **Notifications:**
  - Real-time notifications regarding document submission and application status

- **Document Management:**
  - Upload, store, and review OPT-related documents securely

- **Backend Architecture:**
  - RESTful APIs to support frontend operations
  - Scalable and secure backend built with Node.js and Express.js
  - MongoDB database for document and user data storage

---
## Use Cases

### **International Students Tracking OPT Application**
- **Description:** International students can use the portal to submit their OPT application documents and track the progress of their application.
- **Key Features:**
  - Submit and upload required documents (e.g., I-20, passport copy)
  - View real-time status updates on their application (e.g., Submitted, Under Review, Approved)
  - Receive notifications for any updates or required actions (e.g., document review, missing documents)
  - Secure login and user account management

### **Administrators Reviewing and Managing Applications**
- **Description:** Administrators can review submitted OPT documents and update the status of each application based on their evaluation.
- **Key Features:**
  - Review student-submitted documents
  - Update status (e.g., Pending, Approved, Rejected)
  - Manage and track workflows for multiple student applications
  - Provide feedback or requests for additional documents to students
  - Export application data for reporting purposes

###  **Educational Institutions Streamlining the OPT Process**
- **Description:** Educational institutions can use the portal to manage a large number of international students applying for OPT, ensuring efficient workflow and communication.
- **Key Features:**
  - Centralized dashboard for tracking all student applications
  - Bulk review of student submissions and batch status updates
  - Notifications to students and staff about deadlines and updates
  - Generate reports on the overall status of OPT applications

### **Cross-Campus Collaboration**
- **Description:** University departments, such as the international student office or academic advisors, can collaborate to ensure timely submission of documents and progress tracking.
- **Key Features:**
  - Multiple users with different roles (e.g., Admin, Student)
  - Role-based access control to restrict or allow different actions based on user roles
  - Team collaboration tools (e.g., comment sections, real-time updates)
  - Seamless transition of data across different departments for a smooth review process

### **Notifications and Alerts for Students and Administrators**
- **Description:** Both students and administrators will receive notifications for important milestones in the OPT process, such as document submission, application approval, or required updates.
- **Key Features:**
  - Real-time email or in-app notifications when documents are received, status changes, or feedback is given
  - Alerts for upcoming deadlines and actions required (e.g., document submission)
  - Customizable notification preferences for students and administrators

### **Document Management for OPT Application**
- **Description:** The portal ensures that all required documents are stored securely and can be easily retrieved by students and administrators during the OPT application process.
- **Key Features:**
  - Upload and store documents securely
  - Allow students to submit multiple versions of documents if needed
  - Administrators can download, review, or request resubmission of documents
  - Secure access to sensitive data, such as passport or visa details

###  **Audit and Reporting for OPT Applications**
- **Description:** The portal provides auditing features and generates reports to help administrators monitor application progress, identify bottlenecks, and maintain transparency.
- **Key Features:**
  - Generate reports on the number of applications in each status (e.g., Submitted, Under Review, Approved)
  - View logs of all actions taken on applications (e.g., changes in status, document submission)
  - Export data in various formats (e.g., PDF, CSV) for further analysis
  - Track performance of the application review process for continuous improvement

### **Self-Service for Students**
- **Description:** Students can independently check the status of their applications, view the required documents, and submit or resubmit documents without needing constant interaction with administrators.
- **Key Features:**
  - Self-service dashboard for students to upload documents, check their application status, and receive updates
  - Ability to resubmit or update documents if they were rejected or flagged by administrators
  - Clear communication about what documents are missing or need further attention
---
## Team Structure

### Project Leadership:
 - **Technical Project Manager**: Rahul Ashok Kodate – [kodate.rahulashok@humanitarians.ai](mailto:kodate.rahulashok@humanitarians.ai)  
  _Leading Agile planning, stakeholder communication, sprint execution, and project delivery._

- **Project Manager (Former)**: Gayathri Vummenthala  
- **Assistant Project Manager**: Titiksha Ghosh


### Frontend Team:
- Rolwyn Quadras (Former)
- Rushikesh Deore (Former)
- Rajas Telang(Joined the Backend Team)
- Adithya Narayan Badanidiyoor
- Muskan Rajkumar Kachhela

### Backend Team:
- Saurav Shaw (Former)
- Hrithik Bandaru (Former)
- Xiangyang Liu (Former)
- Priyanka Chaurasia (Former)
- Rajas Telang

### UI/UX Team:
- Pavithra Kareddy (Former)
- Vishrutha Abbaiah

---

## Tech Stack

| Layer       | Technology         |
|-------------|--------------------|
| **Frontend** | React.js, JavaScript, HTML5, CSS3 |
| **Backend**  | Node.js, Express.js |
| **Database** | MongoDB (Mongoose ODM) |
| **Cloud**    | AWS EC2, GitHub Actions |
| **UI/UX**    | Figma              |
| **Version Control** | GitHub           |

---

## Project Structure

```bash
opt-portal-project/
├── backend/                  
│   ├── controllers/          # Business logic for API operations
│   ├── models/               # Mongoose schemas (User, Documents, Application)
│   ├── routes/               # RESTful API endpoints
│   ├── middleware/           # Auth, logging, error handling
│   ├── config/               # DB configs, constants
│   └── server.js             # Backend entry point
│
├── frontend/
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/            # Dashboard and application views
│   │   ├── services/         # API interaction layer
│   │   └── App.js            # Application root
│   └── public/               # Static assets
│
├── .github/                  # CI/CD workflows
├── .env                      # Environment configs (excluded from version control)
├── README.md                 # Project documentation
├── package.json              # Dependency and script management
└── Procfile                  # Optional for Heroku deployment
````

---

## Development & Local Setup

### Prerequisites

* Node.js & npm installed
* MongoDB instance (local or cloud)
* .env file with required variables (MongoDB URI, JWT\_SECRET, etc.)

### Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/Humanitariansai/OPT-Project
   ```

2. **Backend setup**:

   ```bash
   cd opt-portal-backend
   npm install
   npm run dev
   ```

3. **Frontend setup**:

   ```bash
   cd opt-portal-frontend
   npm install
   npm start
   ```

4. **Configure .env** file with:

   * `MONGODB_URI`
   * `JWT_SECRET`
   * Relevant third-party API keys

---

## Demo & Resources

* **Live Demo:** Coming soon (via AWS EC2 or Heroku)
* **Project Document:** [OPT Portal Project Document](https://docs.google.com/document/d/1A398kipS7bGlQUvDpMjV6jIFtex2grjI4v-VrrIOdW4/edit?tab=t.0)
* **Figma Board:** [OPT Portal Figma Design](https://www.figma.com/design/2vUCCEvZ9tZKx6JQTHRNPb/OPT-Portal-second-phase?node-id=0-1&p=f&t=SI9NAMUOy2QyVEaB-0)


---

## Internal Reporting & Expectations

> For all internal team members (Humanitarians.AI)

* **Code contributions must be pushed biweekly**
* **Team members are expected to update the Kanban board regularly**
* **Share weekly status and demo updates (screenshots/video walkthroughs)**
* **Refer to [Reporting Guidelines](https://github.com/nikbearbrown/Humanitarians_AI/tree/main/Fellows)**

---

## GitHub Repositories

* **OPTPortal**: [opt-portal-project](https://github.com/Humanitariansai/OPT-Project)

---

## Contact

For questions, improvements, or demo requests, reach out to:

**Rahul Ashok Kodate**
[kodate.rahulashok@humanitarians.ai](mailto:kodate.rahulashok@humanitarians.ai)

