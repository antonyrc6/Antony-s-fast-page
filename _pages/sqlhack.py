
from flask import Flask, render_template, request, redirect, session
import sqlite3 #import sqlite library for database

app = Flask(__name__)

def register_user(id, student, grade):
    conn = sqlite3.connect('/_notebooks/files/grade.db')
    c = conn.cursor()
    c.execute('INSERT INTO grades(id, student, grade) values (?, ?, ?)', (id, student, grade))
    conn.commit()
    conn.close()

@app.route('/create', methods=["POST", "GET"])
def create():
    if request.method == 'POST':
        id = request.form['id']
        student = request.form['student']
        grade = request.form['grade']

        register_user(id, student, grade)
        return()
    

@app.route('/update', methods=["POST", "GET"])
def update():
    
    conn = sqlite3.connect('/_notebooks/files/grade.db')
    c = conn.cursor()
    
    id = request.form['id']
        
    c.execute("SELECT * FROM grades WHERE id=?", (id,))
    fetch = c.fetchone()
        
    if fetch:
        grade = request.form['grade']
            
        c.execute("UPDATE grades SET grade=? WHERE id=?", (grade, id))
        conn.commit()
            
        return(f"student {id}'s grade has been updated to {grade}")
        
    c.close()
    conn.close()
    

