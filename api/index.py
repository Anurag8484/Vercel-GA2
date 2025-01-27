import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load students data from list.json
with open('list.json') as f:
    students_list = json.load(f)

# Convert list of students into a dictionary
students = {student["name"]: student["marks"] for student in students_list}

@app.route("/")
def home():
    return jsonify({"message":"Welcome"})


@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    marks = [students.get(name, None) for name in names]
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
