import json
import os
from complaint import Complaint


DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "complaints.json"
)


class ComplaintManager:

    def __init__(self):
        self.complaints = []
        self.load_complaints()

    def load_complaints(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                self.complaints = json.load(file)

    def save_complaints(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.complaints, file, indent=4)

    def register_complaint(self, category, description, student_name="Anonymous"):
        complaint = Complaint(category, description, student_name)
        self.complaints.append(complaint.to_dict())
        self.save_complaints()
        return complaint.complaint_id

    def view_complaints(self):
        return self.complaints

    def update_status(self, complaint_id, status):
        for complaint in self.complaints:
            if complaint["complaint_id"] == complaint_id:
                complaint["status"] = status
                self.save_complaints()
                return True
        return False

    def search_complaint(self, complaint_id):
        for complaint in self.complaints:
            if complaint["complaint_id"] == complaint_id:
                return complaint
        return None

