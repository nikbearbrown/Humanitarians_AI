# Kanban Board Project

## Project Overview

The **Kanban Board Project** is a full-stack Agile task management platform built under the **Humanitarians.AI** initiative. This application empowers teams to organize work visually and manage workflows efficiently through a dynamic, real-time Kanban board. Users can drag and drop tasks, collaborate asynchronously, and track progress across customizable stages like **To Do**, **In Progress**, **In Review**, and **Done**.

The project is designed to support cross-functional, distributed teams such as students, NGOs, researchers, and developers. It leverages modern UI/UX design and a scalable backend architecture while adhering to **Agile and Scrum methodologies** to promote transparency, accountability, and velocity in team collaboration.

### Key Features

- Interactive, drag-and-drop Kanban board
- Secure user authentication and role-based access control
- Create, assign, edit, delete, and move tasks between stages
- Team collaboration with real-time updates
- Administrative panel for user and board management
- Modular, extensible, and cloud-ready architecture

---

## Use Cases

- **Academic Capstone and Research Projects**  
  Manage deliverables, coordinate responsibilities, and ensure milestone alignment among students and academic advisors.

- **Non-Profit & NGO Program Management**  
  Enable decentralized teams to manage campaigns, track task completion, and communicate progress efficiently.

- **Hackathons & Innovation Challenges**  
  Facilitate rapid ideation and execution during events with short timelines and collaborative workflows.

- **Volunteer Coordination Platforms**  
  Organize community activities by assigning tasks, monitoring participation, and communicating updates clearly.

- **Agile Engineering Teams**  
  Support Scrum ceremonies, backlog grooming, sprint tracking, and stakeholder visibility through a flexible task board.

- **Remote & Distributed Teams**  
  Enhance cross-timezone collaboration by providing a centralized workspace that ensures visibility and progress continuity.

---

## Project Objectives

1. Deliver a highly usable Kanban board interface with core CRUD task operations  
2. Ensure performance, security, and responsiveness across web clients  
3. Foster asynchronous collaboration through real-time updates and notifications  
4. Build a scalable and modular backend architecture using RESTful APIs  
5. Automate Agile workflows with task statuses, prioritization, and sprint visualization  
6. Deploy the application on the cloud with CI/CD support for production-ready environments

---

## Team Structure

### Project Leadership
- **Technical Project Manager**: Rahul Ashok Kodate – [kodate.rahulashok@humanitarians.ai](mailto:kodate.rahulashok@humanitarians.ai)  
  _Leading Agile planning, stakeholder communication, sprint execution, and project delivery._

- **Project Manager (Former)**: Gayathri Vummenthala  
- **Assistant Project Manager**: Titiksha Ghosh

### Development Team

**Frontend Team**  
- Manan Gandhi *(Former)*  
- Vrushank Hiremath *(Former)*  
- Sai Sudheer *(Former)*  
- Adhyantini Bogawat *(Former)*  
- Shubhi Miradwal *(Former)*  
- Pranjal Sharma *(Former)*  
- Juan Diego Dumez Garcia

**Backend Team**  
- Natarajan Lekshmi Narayana Pillai *(Former)*  
- Roshan Dadlani *(Former)*  
- Ujwal Gupta *(Former)*  
- Hitesh Pant

**UI/UX Team**  
- Shrimoyee Banerjee *(Former)*  
- Sai Supriya Komarraju *(Former)*  
- Sagar Yogesh Mehta

---

## Tech Stack

| Layer        | Technologies                        |
|--------------|-------------------------------------|
| **Frontend** | React.js, JavaScript, HTML5, CSS3   |
| **Backend**  | Node.js, Express.js                 |
| **Database** | MongoDB (Mongoose ODM)              |
| **Cloud**    | AWS EC2, GitHub Actions             |
| **UI/UX**    | Figma                                |
| **Version Control** | GitHub                        |

---

## Project Structure

```bash
kanban-board/
├── backend/                  
│   ├── controllers/          # Business logic for API operations
│   ├── models/               # Mongoose schemas (Task, User, Board)
│   ├── routes/               # RESTful API endpoints
│   ├── middleware/           # Auth, logging, error handling
│   ├── config/               # DB configs, constants
│   └── server.js             # Backend entry point
│
├── frontend/
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/            # Dashboard and Kanban views
│   │   ├── services/         # API interaction layer
│   │   └── App.js            # Application root
│   └── public/               # Static assets
│
├── .github/                  # CI/CD workflows
├── .env                      # Environment configs (excluded)
├── README.md                 # Project documentation
├── package.json              # Dependency and script management
└── Procfile                  # Optional for Heroku deployment
````

---

## Development & Local Setup

### Prerequisites

* Node.js & npm installed
* MongoDB instance (local or cloud)
* `.env` file with required variables

### Setup Instructions

1. **Clone the repositories:**

   ```bash
   git clone https://github.com/Humanitariansai/kanban-board-frontend
   git clone https://github.com/Humanitariansai/kanban-board-backend
   ```

2. **Backend setup:**

   ```bash
   cd kanban-board-backend
   npm install
   npm run dev
   ```

3. **Frontend setup:**

   ```bash
   cd kanban-board-frontend
   npm install
   npm start
   ```

>  Configure `.env` file with:
> `MONGODB_URI`, `JWT_SECRET`, and relevant third-party API keys.

---

## Demo & Resources

* **Live Demo**: *Coming soon* (via AWS EC2 or Heroku)
* **Deliverables & Planning**: [Project Document](https://docs.google.com/document/d/1A398kipS7bGlQUvDpMjV6jIFtex2grjI4v-VrrIOdW4/edit?usp=sharing)
* **Scrum Board**: [Figma Kanban Tracker](https://www.figma.com/board/mxMNKcci5hSlNWAdd406BF/OPT-Portal-and-Kanban-Board-Project)


## Internal Reporting & Expectations

> For all internal team members (Humanitarians.AI)

* **Code contributions must be pushed biweekly**
* **Team members are expected to update the Kanban board regularly**
* **Share weekly status and demo updates (screenshots/video walkthroughs)**
* **Refer to [Reporting Guidelines](https://github.com/nikbearbrown/Humanitarians_AI/tree/main/Fellows)**

---

## GitHub Repositories

* **Frontend**: [kanban-board-frontend](https://github.com/Humanitariansai/kanban-board-frontend)
* **Backend**: [kanban-board-backend](https://github.com/Humanitariansai/kanban-board-backend)



## Contact

For questions, improvements, or demo requests, reach out to:

**Rahul Ashok Kodate**
[kodate.rahulashok@humanitarians.ai](mailto:kodate.rahulashok@humanitarians.ai)

---

