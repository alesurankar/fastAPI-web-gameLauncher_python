# python app_flask.py

from flask import Flask, render_template, request, redirect, url_for, session
import requests 



app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
FASTAPI_URL = "http://127.0.0.1:8000"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username

        # Create a table for this user (if it doesn't exist)
        requests.post(f"{FASTAPI_URL}/create-user/{username}")
        return redirect(url_for('profile'))

    return render_template('login.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']

    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])

        # Add character via FastAPI
        r = requests.post(f"{FASTAPI_URL}/add-character/{username}", json={"name": name, "age": age})
        return f"Character Added: {r.json()}"

    # GET user list
    r = requests.get(f"{FASTAPI_URL}/list-character/{username}")
    characters = r.json()

    return render_template('profile.html', username=username, characters=characters)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()

        if not username:
            return "Username is required.", 400

        try:
            r = requests.post(f"{FASTAPI_URL}/create-user/{username}")
        except Exception as e:
            return f"Error connecting to FastAPI: {str(e)}", 500

        if r.status_code == 200:
            return redirect(url_for('login'))
        else:
            return f"Registration failed: {r.json().get('detail', 'Unknown error')}", 400

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True, port=5000)