# Task Management API 🔐

A role-based **Task Management REST API** built with **Django REST Framework (DRF)** and **JWT Authentication**. This project demonstrates secure authentication, role-based authorization, task assignment, task completion reporting, and RESTful API design.

## 🚀 Features

### Authentication

* JWT Authentication using Simple JWT
* User Registration
* Login (Access & Refresh Tokens)
* Token Refresh

### Role-Based Access Control

#### Super Admin

* Create Admin accounts
* Delete Admin accounts
* Promote Admin → Super Admin
* Demote Admin → User/Admin
* Create, Update and Delete Users
* Assign roles
* View all tasks
* Full system access

#### Admin

* Create tasks
* Assign tasks to users
* View and manage assigned tasks
* View task completion reports
* Limited administrative privileges

#### User

* View only assigned tasks
* Update task status
* Submit completion report
* Submit worked hours
* Cannot access other users' tasks

---

## 📋 Task Workflow

1. Super Admin creates Admin accounts.
2. Admin creates tasks.
3. Admin assigns tasks to users.
4. User updates task status.
5. When marking a task as **Completed**, the user must provide:

   * Completion Report
   * Worked Hours
6. Admin and Super Admin can review completed task reports.

---

## 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT
* SQLite
* drf-spectacular (Swagger / OpenAPI Documentation)

---

## 🔐 Authentication

This API uses **JWT Authentication**.

### Obtain Token

```http
POST /api/token/
```

### Refresh Token

```http
POST /api/token/refresh/
```

After authentication, include the access token in every protected request:

```text
Authorization: Bearer <access_token>
```

---

## 📚 API Documentation

Interactive API documentation is available using Swagger UI.

```
/api/docs/
```

OpenAPI schema:

```
/api/schema/
```

ReDoc:

```
/api/redoc/
```

---

## 📦 Main API Endpoints

### Authentication

* Register User
* Login
* Refresh Token

### User Management

* Create User
* Update User
* Delete User
* Promote User
* Demote User
* Assign Roles

### Task Management

* Create Task
* List Tasks
* Retrieve Task
* Update Task
* Delete Task
* Assign Task
* Submit Completion Report
* View Completion Report

---

## 🔒 Permissions

| Role        | Permissions                            |
| ----------- | -------------------------------------- |
| Super Admin | Full access to users, admins and tasks |
| Admin       | Manage tasks assigned within scope     |
| User        | Access only own tasks                  |

---

## ✅ Validation Rules

* Only authenticated users can access protected endpoints.
* Users can only view and update their own tasks.
* Completion Report and Worked Hours are mandatory when a task is marked as **Completed**.
* Admins cannot perform Super Admin operations.
* Role-based permissions are enforced throughout the API.

---

## 🗄 Database

* SQLite

---
