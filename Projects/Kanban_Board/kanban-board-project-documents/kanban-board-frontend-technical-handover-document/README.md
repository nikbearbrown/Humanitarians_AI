# Kanban Board Frontend

## Project Overview
This is the frontend application for the Kanban Board system, designed to support user roles such as Admin, Project Manager (PM), and Volunteer. Built using React with Vite and styled with Tailwind CSS, the application includes authentication flows, routing, and responsive design.

## Tech Stack
| Category       | Technology                    |
|----------------|-------------------------------|
| Framework      | React (Vite-based)            |
| Styling        | Tailwind CSS                  |
| Routing        | React Router                  |
| CI/CD          | GitLab CI                     |
| Linting        | ESLint                        |
| Build Tool     | Vite                          |

## Local Setup Instructions

1. Clone the repository:
```bash
git clone <repo-url>
cd Frontend_Kanban
````

2. Install dependencies:

```bash
npm install
```

3. Update API endpoints to use local backend:

* In `.env`, set:

```env
VITE_API_URL_PROJECTS="http://localhost:3000/api/projects/"
```

4. Run the app:

```bash
npm run dev
```

5. Visit the app at:

```
http://localhost:5173
```

6. To test with authentication:

* Register a user via Postman:
  `POST http://localhost:3000/api/auth/register`
* Login:
  `POST http://localhost:3000/api/auth/login`
* Copy the returned JWT token and use it in Authorization headers for protected routes.

## Folder Structure

```bash
Frontend_Kanban/
├── .env                         # Environment variables
├── .gitlab-ci.yml              # GitLab CI/CD pipeline
├── public/                     # Static public files
├── node_modules/              # Dependencies
├── images/                    # Static assets
├── src/
│   ├── adminComponents/        # Admin-specific components
│   ├── pmComponents/           # Project Manager components
│   ├── volunteerComponents/    # Volunteer components
│   ├── assets/                 # Fonts, icons, and images
│   ├── App.jsx                 # Root component
│   ├── login.jsx               # Login screen
│   ├── forgotPassword.jsx     # Forgot Password page
│   ├── resetPassword.jsx      # Reset Password page
│   ├── main.jsx                # Post-login entry point
│   ├── pageNotFound.jsx       # 404 page
│   └── successMessage.jsx     # Generic success screen
├── vite.config.js             # Vite configuration
├── tailwind.config.js         # Tailwind customization
├── eslint.config.js           # ESLint rules
├── branching-strategy.md      # Git strategy guide
└── README.md                  # Project documentation
```

## Environment Variables (.env)

```env
VITE_GAPI_CLIENT_ID="1067817291108-xxxxxx.apps.googleusercontent.com"
VITE_SERVICE_ID="service_xxxxxx"
VITE_TEMPLATE_ID="template_n4ilima"
VITE_PRIVATE_KEY="your_private_key_here"
VITE_JWT_TOKEN="your_jwt_token_here"
VITE_API_URL_PROJECTS="http://localhost:3000/api/projects/"
```

> Note: Update `VITE_API_URL_PROJECTS` to production endpoint once backend is deployed on AWS.

## Build & Deployment

Build the project:

```bash
npm run build
```

CI/CD is managed using GitLab pipelines via `.gitlab-ci.yml`.

## Work Summary (Frontend Contributions)

**Contributor:** Pranjal Sharma
**Branch:** `pranjal-dev`

* Improved UI/UX for Project Admin Page
* Added count indicators to each Kanban column
* Implemented action buttons:

  * Scheduled Meeting
  * View Team Members
  * Add Task
* Admin Home Page enhancements:

  * Reminder Panel
  * Task Summary Section

## Pending Work / Known Issues

* Create Task page still has unresolved issues
* Drag-and-drop has occasional glitches
* Additional UI polish and bug fixing required

## Gotchas & Tips

* Tailwind spacing is overridden via `tailwind.config.js`
* Clear API mocks when switching environments
* Kanban board state is stored in `localStorage` — clear it when testing board resets

---

For questions or contributions, please open an issue or pull request in the repository.

```

