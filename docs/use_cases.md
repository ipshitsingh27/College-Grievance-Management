# Use Case Documentation

## 1. Actors

### Student
The student can:
- Register a complaint.
- Submit a complaint anonymously.
- Receive a unique complaint ID.
- Search for an existing complaint.
- Check complaint status.

### Administrator
The administrator can:
- View registered complaints.
- Search complaints.
- Update complaint status.
- Review complaint records.

Note: Administrator operations in the current prototype are performed through the command-line interface without authentication.

## 2. Use Case Descriptions

### Use Case 1: Register Complaint
- Actor: Student
- Input: Student name, complaint category and description.
- Process: System creates a complaint record and generates a unique ID.
- Output: Complaint ID is displayed.

### Use Case 2: View Complaints
- Actor: Administrator
- Input: Select view complaints option.
- Process: System retrieves stored complaint records.
- Output: List of registered complaints.

### Use Case 3: Search Complaint
- Actor: Student / Administrator
- Input: Complaint ID.
- Process: System searches for the matching record.
- Output: Complaint details or a not-found message.

### Use Case 4: Update Complaint Status
- Actor: Administrator
- Input: Complaint ID and new status.
- Process: System updates the selected complaint.
- Output: Confirmation of successful update.

## 3. Complaint Status

| Status | Description |
|---|---|
| Pending | Complaint has been registered. |
| Under Review | Complaint is being reviewed. |
| Resolved | Complaint has been marked resolved. |

## 4. General Workflow

1. Student submits a complaint.
2. System generates a complaint ID.
3. Complaint is saved in the records.
4. Administrator views and reviews complaints.
5. Administrator updates the status.
6. Complaint status can be checked using its ID.

## 5. Exception Scenarios

- Empty complaint records.
- Invalid complaint ID.
- Invalid status selection.
- Missing complaint description.
