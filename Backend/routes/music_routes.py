from flask import Blueprint, jsonify

music_bp = Blueprint('music_bp', __name__)

@music_bp.route('/', methods=['GET'])
def get_music():
    return jsonify({"message": "Music route working!"})
