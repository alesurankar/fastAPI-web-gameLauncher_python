# python app_flask.py

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# FastAPI URL for data
FASTAPI_URL = "http://127.0.0.1:8000/users"

@app.route('/')
def home():
    # Fetch data from FastAPI
    try:
        response = requests.get(FASTAPI_URL)
        users = response.json()
    except Exception as e:
        users = []
        print(f"Error fetching users from FastAPI: {e}")
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Flask runs on port 5000
