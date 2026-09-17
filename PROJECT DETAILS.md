# Placement Management System

A web-based Placement Management System developed to manage student, company, and placement information in one application.

## Features

* Student Management
* Company Management
* Placement Management
* Add, Edit and Delete Records
* Search Functionality
* Input Validation
* Placement Status Tracking
* Dashboard Statistics

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Django
* Django REST Framework

### Database

* SQLite

## Project Modules

### Student Management

Manages student details such as name, register number, department, email, phone number and CGPA.

### Company Management

Manages company details such as company name, job role, package, eligibility CGPA and location.

### Placement Management

Manages student placements, company details, job role, placement status and placement date.

### Dashboard

Displays placement-related statistics such as total students, total companies, total placements, selected students, applied placements, rejected placements and selection percentage.

## Project Structure

```text
Placement-Management-System/
│
├── backend/
│   ├── config/
│   ├── students/
│   ├── manage.py
│   └── db.sqlite3
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   ├── company.html
│   ├── company.js
│   ├── placement.html
│   ├── placement.js
│   └── dashboard.html
│
└── README.md
```

## How to Run

### Backend

Open the backend folder in the terminal and run:

```bash
python manage.py runserver
```

The Django backend will run on:

```text
http://127.0.0.1:8000/
```

### Frontend

Open the frontend folder using VS Code and run the HTML files using **Live Server**.

## API Endpoints

```text
/api/students/
/api/companies/
/api/placements/
```

## Conclusion

The Placement Management System provides a simple and efficient way to manage student, company and placement information using a web-based application.
