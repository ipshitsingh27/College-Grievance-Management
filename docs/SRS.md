# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose
The purpose of the College Complaint and Grievance Management System is to provide a structured platform for students to report college-related complaints and grievances.

### 1.2 Scope
The proposed system focuses on recording, managing and tracking complaints related to:
- Ragging
- Bullying
- Harassment
- Misbehaviour
- Discrimination
- Infrastructure issues

### 1.3 Intended Users
- Students
- College Administration
- Grievance Committee

## 2. Overall Description

The system is designed to simplify the complaint registration and management process. It maintains complaint records and allows authorized users to review and update complaint statuses.

## 3. Functional Requirements

1. The system shall allow students to register complaints.
2. The system shall generate a unique complaint ID.
3. The system shall support anonymous complaint registration.
4. The system shall store complaint details.
5. The system shall allow viewing registered complaints.
6. The system shall allow searching complaints using complaint ID.
7. The system shall support complaint status updates.
8. The system shall maintain complaint records in JSON format.

## 4. Non-Functional Requirements

- Usability: The system should be easy to understand.
- Reliability: Complaint records should be stored consistently.
- Maintainability: The source code should be modular.
- Privacy: Sensitive complaint information should have restricted access in a production deployment.
- Performance: Basic operations should execute efficiently.

## 5. Hardware Requirements

- Computer or laptop
- Minimum 4 GB RAM
- Basic storage space

## 6. Software Requirements

- Operating System: macOS / Windows / Linux
- Programming Language: Python 3
- Data Storage: JSON
- Code Editor: VS Code or any Python editor

## 7. System Constraints

- The current implementation is command-line based.
- JSON files are used instead of a database server.
- Authentication and role-based access control are not implemented.
- The project is an academic prototype and is not suitable for handling real sensitive complaints.

## 8. Future Enhancements

- Web-based user interface
- Secure student authentication
- Administrator dashboard
- Email notifications
- Encrypted complaint storage
- Role-based access control
- Complaint analytics and reports

## 9. Conclusion

The proposed system aims to improve the organization and tracking of college grievances through a simple and structured software solution.
