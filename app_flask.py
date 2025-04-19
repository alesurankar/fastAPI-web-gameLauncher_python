# python app_flask.py

from flask import Flask, render_template, request, redirect, url_for
from app_database import create_table, insert_data, retrieve_data, delete_table

app = Flask(__name__)

@app.route('/')
def home():
    users = retrieve_data()
    return render_template("index.html", users=users)

@app.route('/create_table')
def create():
    create_table()
    return redirect(url_for('home'))

@app.route('/delete_table')
def delete():
    delete_table()
    return redirect(url_for('home'))

@app.route('/insert_data', methods=['POST'])
def insert():
    name = request.form['name']
    age = request.form['age']
    insert_data(name, age)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
