from flask import Blueprint, request, jsonify
from models.assignment import Assignment

assignment_bp = Blueprint("assignment_bp", __name__)

# ADD ASSIGNMENT
@assignment_bp.route("/assignments", methods=["POST"])
def add_assignment():
    data = request.get_json()

    subject_id = data.get("subject_id")
    title = data.get("title")
    deadline = data.get("deadline")

    if not subject_id or not title:
        return jsonify({"error": "Subject ID and title required"}), 400

    Assignment.create(subject_id, title, deadline)

    return jsonify({"message": "Assignment added successfully"})


# GET ASSIGNMENTS BY SUBJECT
@assignment_bp.route("/assignments/<int:subject_id>", methods=["GET"])
def get_assignments(subject_id):
    assignments = Assignment.get_by_subject(subject_id)

    assignment_list = []

    for a in assignments:
        assignment_list.append({
            "id": a[0],
            "title": a[1],
            "deadline": a[2],
            "status": a[3],
            "created_at": a[4]
        })

    return jsonify(assignment_list)

# UPDATE ASSIGNMENT STATUS
@assignment_bp.route("/assignments/<int:assignment_id>", methods=["POST"])
def update_assignment_status(assignment_id):
    data = request.get_json()
    status = data.get("status")

    if not status:
        return jsonify({"error": "Status required"}), 400

    Assignment.update_status(assignment_id, status)

    return jsonify({"message": "Assignment status updated successfully"})