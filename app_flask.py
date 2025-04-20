# python app_flask.py

from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests 
import os



app = Flask(__name__)
app.secret_key = os.urandom(24)
FASTAPI_URL = "http://127.0.0.1:8000"

@app.route('/')
def index():
    username = session.get('username', None)

    try:
        response = requests.get(f"{FASTAPI_URL}/list-users")
        tables = response.json().get("tables", [])
    except Exception:
        tables = []

    return render_template("index.html", username=username, tables=tables)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        check_url = f"{FASTAPI_URL}/check-users/{username}"

        try:
            response = requests.get(check_url)
            response.raise_for_status()
            exists = response.json().get("exists", False)

            if exists:
                session['username'] = username
                return redirect(url_for('profile'))
            else:
                flash("User does not exist.")
        except requests.exceptions.RequestException as e:
            flash(f"Error checking user: {e}")

    return render_template('login.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']

    if request.method == 'POST':
        name = request.form['name']
        level = int(request.form['level'])

        # Add character via FastAPI
        r = requests.post(f"{FASTAPI_URL}/add-character/{username}", json={"name": name, "level": level})
        if r.status_code == 200:
            flash("Character added successfully!")
        else:
            flash(f"Failed to add character: {r.json().get('detail', 'Unknown error')}")
        
        return redirect(url_for('profile'))

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
            session['username'] = username
            return redirect(url_for('profile'))
        else:
            return f"Registration failed: {r.json().get('detail', 'Unknown error')}", 400

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True, port=5000)