import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load students data from list.json
with open('list.json') as f:
    students_list = json.load(f)

# Create a dictionary where the keys are student names and the values are the first encountered marks
students = {}

# Populate the dictionary with the first occurrence of each student name
for student in students_list:
    if student["name"] not in students:
        students[student["name"]] = student["marks"]

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    marks = [students.get(name, None) for name in names]
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
