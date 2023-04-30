from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# create a function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('/_notebooks/files/grade.db')
    conn.row_factory = sqlite3.Row
    return conn

# create a route for creating a profile
@app.route('/create-form', methods=['GET', 'POST'])
def create_profile():
    if request.method == 'POST':
        # get the input values from the form
        id = request.form['id']
        name = request.form['name']
        grade = request.form['grade']

        # insert the profile into the database
        conn = get_db_connection()
        conn.execute('INSERT INTO students (id, name, grade) VALUES (?, ?, ?)', (id, name, grade))
        conn.commit()
        conn.close()

        # return a success message
        return jsonify({'message': 'Profile created successfully!'})

    # if it's a GET request, render the create profile template
    return render_template('./sql_frontend.html')

# create a route for reading a profile
@app.route('/read-form', methods=['GET', 'POST'])
def read_profile():
    if request.method == 'POST':
        # get the input value from the form
        id = request.form['id']

        # select the profile from the database
        conn = get_db_connection()
        profile = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
        conn.close()

        # render the profile template with the selected profile data
        return render_template('./sql_frontend.html', profile=profile)

    # if it's a GET request, render the read profile template
    return render_template('./sql_frontend.html')

# create a route for updating a profile
@app.route('/update-form', methods=['GET', 'POST'])
def update_profile():
    if request.method == 'POST':
        # get the input values from the form
        id = request.form['id']
        grade = request.form['grade']

        # update the profile in the database
        conn = get_db_connection()
        conn.execute('UPDATE students SET grade = ? WHERE id = ?', (grade, id))
        conn.commit()
        conn.close()

        # return a success message
        return jsonify({'message': 'Profile updated successfully!'})

    # if it's a GET request, render the update profile template
    return render_template('./sql_frontend.html')

# create a route for deleting a profile
@app.route('/delete-form', methods=['GET', 'POST'])
def delete_profile():
    if request.method == 'POST':
        # get the input value from the form
        id = request.form['id']

        # delete the profile from the database
        conn = get_db_connection()
        conn.execute('DELETE FROM students WHERE id = ?', (id,))
        conn.commit()
        conn.close()

        # return a success message
        return jsonify({'message': 'Profile deleted successfully!'})

    # if it's a GET request