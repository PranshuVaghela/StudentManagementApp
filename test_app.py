import unittest
from app import app

class StudentAppTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Student Management System", response.data)

    def test_students(self):
        response = self.client.get("/students")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()