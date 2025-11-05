# Employee Resource Management PWA

## Overview
A progressive web app built with Flask and PostgreSQL for employee resource management. Project managers can search employees by skills, availability status, and other criteria to make informed project assignment decisions.

## Purpose
- Help project managers understand employee utilization across the organization
- Track employee availability for project assignments
- Search employees by name, email, and skills
- Mobile-friendly interface for on-the-go access

## Features
- **Public Access**: Anyone can view employee directory and search
- **Employee Login**: Login with Employee ID to update personal profile
- **Availability Tracking**: Toggle button to mark availability status (deployed/available)
- **Search & Filter**: Search by name, email, skills with availability filter
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **PWA Support**: Installable on mobile devices

## Tech Stack
- **Backend**: Flask, SQLAlchemy, Flask-Login
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **PWA**: Service Worker, Web App Manifest

## Project Structure
```
├── app.py              # Main Flask application
├── models.py           # Database models
├── init_db.py          # Database initialization with dummy data
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   └── profile.html
└── static/             # Static assets
    ├── css/
    │   └── style.css
    ├── js/
    │   └── app.js
    ├── manifest.json
    └── sw.js
```

## Recent Changes
- 2025-11-05: Initial project setup with Flask, PostgreSQL integration
- 2025-11-05: Added employee models with availability tracking
- 2025-11-05: Implemented search and filter functionality
- 2025-11-05: Created responsive UI with PWA support

## Database Schema
- **Employee Table**: id, employee_id (unique), name, email, role, location, skills, is_available
- Uses PostgreSQL for data persistence

## User Preferences
- Minimalist and classy UI design
- Mobile-first responsive design
- Simple employee ID-based authentication
