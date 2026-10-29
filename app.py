from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Rahul", "course": "Computer Science"},
    {"id": 2, "name": "Priya", "course": "Computer Science"},
    {"id": 3, "name": "Aman", "course": "Computer Science"}
]

@app.route("/")
def home():
    return "Student Management System - Version 2"

@app.route("/students")
def get_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)