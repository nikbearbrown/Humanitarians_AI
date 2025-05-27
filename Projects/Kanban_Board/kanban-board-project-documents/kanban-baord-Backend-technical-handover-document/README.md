# Kanban Board System

## Project Overview
The **Kanban Board Project** is a centralized project management solution built for **Humanitarians_AI**. This system helps manage, assign, and track tasks for volunteers, ensuring projects progress smoothly from initiation to completion.

## Purpose
- Enable transparent project and task tracking.
- Assign tasks with accountability.
- Centralize communication and task updates.
- Ensure real-time monitoring and efficient resource allocation.

## Tech Stack
| Layer          | Technology                     |
|----------------|----------------------------------|
| Backend        | Node.js, Express.js             |
| Database       | MongoDB, Mongoose               |
| Cloud          | AWS S3                          |
| Auth           | JWT                             |
| API Docs       | Swagger                         |
| File Uploads   | multer, @aws-sdk/client-s3      |

## Project Structure
```bash
kanban-board/
├── app.js                     # Express app config
├── server.js                  # Entry point
├── .env                       # Environment variables
├── config/
│   ├── s3UploadConfig.js      # AWS S3 setup
│   └── swaggerConfig.js       # Swagger setup
├── controllers/              # All route controllers
├── middlewares/              # JWT, role-based auth
├── models/                   # Mongoose schemas
├── routes/                   # Express routes
├── services/                 # Business logic
└── swagger/                  # Swagger documentation
````

## Environment Variables (.env)

```
PORT=3000
MONGODB_URI=<MongoDB Connection String>
JWT_SECRET=<JWT Secret Key>
EMAIL_USER=<SMTP Email Address>
EMAIL_PASS=<SMTP App Password>
FRONTEND_URL=<Frontend Base URL>
AWS_ACCESS_KEY_ID=<AWS Key ID>
AWS_SECRET_ACCESS_KEY=<AWS Secret>
AWS_REGION=us-east-2
AWS_BUCKET_NAME=<Bucket Name>
```

## Core Modules & Files

### app.js

* Sets up middleware (CORS, JSON parsing)
* Connects to MongoDB
* Initializes routes
* Swagger UI at /api-docs

### server.js

* Starts the server on the given PORT

### config/s3UploadConfig.js

* Configures multer-s3 for file uploads to AWS S3

### config/swaggerConfig.js

* Uses swagger-jsdoc and mongoose-to-swagger to auto-generate API docs

## Models

* User.js: Roles (Admin, PM, Volunteer), profile, tasks, projects
* Project.js: Core unit of work, linked to tasks, users
* Task.js: Status (Not Started/In Progress/Completed), linked to projects
* Comment.js: Linked to tasks and users
* TeamGroup.js: Groups of users within projects
* Notification.js: User alerts and updates

## Services

Modular services to separate logic from controllers:

* authService: Login, register, password reset
* userService: CRUD operations for users
* projectService: Manage project lifecycle
* taskService: Task creation and updates
* commentService: Add/update/delete comments
* notificationService: Manage in-app notifications
* authzService: Role verification
* teamGroupService: Team group ops & user mappings

## Middleware

* authMiddleware.js: JWT token verification
* authzMiddleware.js: Role-based access control

## Controllers

Each controller handles incoming requests and integrates with services:

* authController.js: Register/Login/Forgot Password
* authzController.js: Role assignment
* userController.js: CRUD & profile image handling
* projectController.js: Create/Edit/Delete projects
* taskController.js: Manage tasks
* commentController.js: Manage comments
* notificationController.js: Manage notifications
* teamGroupController.js: Manage team groups

## Routes

All APIs follow RESTful conventions:

* Auth: /auth/register, /auth/login, /auth/forgot-password, /auth/reset-password
* Authorization: /assign-role/\:id
* Users: /users, /users/\:id
* Projects: /projects, /projects/\:id, add-users, remove-users
* Tasks: /api/tasks, /api/tasks/\:id
* Comments: /api/comments, /api/comments/\:id
* Notifications: /api/notifications, /api/notifications/\:id
* Team Groups: /team-groups, /team-groups/\:id, add-users, remove-users

## Swagger API Docs

Available at [http://localhost](http://localhost):<PORT>/api-docs

* Integrated with JSDoc & Mongoose schemas
* Supports tagging, grouping, and model schema definitions

## Deployment Notes

* Hosted on AWS
* S3 used for static files/profile images
* Ensure .env is configured correctly before deployment

```
