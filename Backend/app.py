from flask import Flask, jsonify
from flask_cors import CORS # Assuming you are using CORS

app = Flask(__name__)
CORS(app)

# 1. Define dummy data for the tracks (or pull from a database)
DUMMY_TRACKS = [
    {"id": 1, "title": "Amapiano Groove", "artist": "DJ Mzansi", "duration": "3:45"},
    {"id": 2, "title": "Gqom Power", "artist": "King Beat", "duration": "4:01"},
    {"id": 3, "title": "Kwaito Revival", "artist": "The Legends", "duration": "3:20"},
    
]


# 2. Define the main API route that the React app fetches
@app.route("/")
def index():

    return jsonify({
        "message": "API connection successful! Data is ready.",
        "tracks": DUMMY_TRACKS
    })

if __name__ == "__main__":
    app.run(debug=True)