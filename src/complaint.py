from datetime import datetime
import uuid


class Complaint:
    def __init__(self, category, description, student_name="Anonymous"):
        self.complaint_id = str(uuid.uuid4())[:8].upper()
        self.student_name = student_name
        self.category = category
        self.description = description
        self.status = "Pending"
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "complaint_id": self.complaint_id,
            "student_name": self.student_name,
            "category": self.category,
            "description": self.description,
            "status": self.status,
            "date": self.date
        }
