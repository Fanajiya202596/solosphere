from flask import Blueprint, request, jsonify
from models.subjects import Subject

# create Blueprint
subject_bp = Blueprint("subject_bp", __name__)


# ADD SUBJECT
@subject_bp.route("/subjects", methods=["POST"])
def add_subject():
    data = request.get_json()
    name = data.get("name")

    if not name:
        return jsonify({"error": "Subject name required"}), 400

    Subject.create(name)

    return jsonify({"message": "Subject added successfully"})


# GET ALL SUBJECTS
@subject_bp.route("/subjects", methods=["GET"])
def get_subjects():
    subjects = Subject.get_all()

    subject_list = []

    for s in subjects:
        subject_list.append({
            "id": s[0],
            "name": s[1],
            "created_at": s[2]
        })

    return jsonify(subject_list)