🎓 Student Achievement System (SAS)
A comprehensive web-based application designed to manage, track, and analyze student achievements (Academic, Sports, Cultural, etc.). Built using Django (Python) and MySQL, this project demonstrates key Database Management System (DBMS) concepts including Relational Schema, Normalization, JOINs, and Aggregation.

🚀 Features:
Core Functionality
Student Management (CRUD): Add, View, Edit, and Delete student profiles.

Achievement Tracking: Upload achievements with descriptions, dates, and proof files.

Category Management (Master Data): Dynamic creation of achievement categories (e.g., Sports, Academic) with validation.

Status Workflow: Approval system for achievements (Pending, Approved, Rejected).

DBMS & Technical Highlights
Relational Database: Implements One-to-Many relationships (Student → Achievements, Category → Achievements).

Advanced SQL Operations:

JOINs: "Master Report" view combines data from three normalized tables.

Aggregation: Dashboard analytics showing counts and statistics.

Filtering & Sorting: Search functionality and ordering by date/name.

Data Integrity: Uses Foreign Keys and ON DELETE protection to prevent data inconsistency.

Modern UI: Responsive design using Bootstrap 5 and Crispy Forms.

🛠️ Tech Stack
Frontend: HTML5, CSS3, Bootstrap 5, JavaScript.

Backend: Python 3.x, Django Framework.

Database: MySQL Server 8.0.

Tools: VS Code, Git.