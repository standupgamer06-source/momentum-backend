# focus_os/backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask App
app = Flask(__name__)
CORS(app) # Allows Flutter app to talk to the server

# Initialize Firebase Admin SDK
# NOTE: Replace 'path/to/your/serviceAccountKey.json' 
# with the actual path if you didn't save it as 'serviceAccountKey.json' 
# in this same folder.
# D:\focus_os\backend\app.py

cred = credentials.Certificate("focusos-f04ec-firebase-adminsdk-fbsvc-d18caca1c8.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/api/generate_schedule', methods=['POST'])
def generate_schedule():
    """
    Placeholder endpoint for AI schedule generation.
    In a real app, this would call a large language model (LLM).
    """
    data = request.json
    user_input = data.get('input', 'Default user goals.')
    
    # --- AI Logic Placeholder ---
    # Here, a real application would pass 'user_input' to an LLM 
    # to generate a workout or focus plan.
    
    # Mocking a simple, rule-based response for now
    if "strength" in user_input.lower():
        mock_plan = {
            "type": "Strength Focus",
            "description": "AI suggests a 30-minute high-intensity interval circuit focusing on heavy compounds: Squats, Push-ups, and Plank holds (3 sets of 10 reps/30s each).",
            "routine": "compound_focus"
        }
    else:
        mock_plan = {
            "type": "Endurance Focus",
            "description": "AI suggests a 40-minute endurance session: 10 mins jogging, 30 mins focused on high-rep Calisthenics (Lunges, Dips).",
            "routine": "endurance_light"
        }

    return jsonify({"success": True, "schedule": mock_plan})

@app.route('/', methods=['GET'])
def home():
    """Simple check to confirm the server is running."""
    return "FocusOS Backend is Running!"

if __name__ == '__main__':
    # Flask runs on port 5000 by default
    # Host '0.0.0.0' allows connections from the Android Emulator
    app.run(host='0.0.0.0', port=5000)