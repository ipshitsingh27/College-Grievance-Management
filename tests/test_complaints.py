import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.abspath("src"))

from complaint import Complaint
from manager import ComplaintManager


class TestComplaintSystem(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()
        with open(self.temp_file.name, "w") as file:
            file.write("[]")

        import manager
        self.original_file = manager.DATA_FILE
        manager.DATA_FILE = self.temp_file.name

        self.manager = ComplaintManager()

    def tearDown(self):
        import manager
        manager.DATA_FILE = self.original_file
        os.remove(self.temp_file.name)

    def test_complaint_creation(self):
        complaint = Complaint("Bullying", "Test description")
        self.assertEqual(complaint.category, "Bullying")
        self.assertEqual(complaint.status, "Pending")

    def test_register_complaint(self):
        complaint_id = self.manager.register_complaint(
            "Ragging", "Test complaint", "Student"
        )
        self.assertIsNotNone(self.manager.search_complaint(complaint_id))

    def test_update_status(self):
        complaint_id = self.manager.register_complaint(
            "Harassment", "Test complaint"
        )
        result = self.manager.update_status(complaint_id, "Resolved")
        self.assertTrue(result)

    def test_search_invalid_complaint(self):
        result = self.manager.search_complaint("INVALID")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
