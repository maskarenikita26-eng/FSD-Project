from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_connection, create_table

app = Flask(__name__)
app.secret_key = "student_portal_secret_key_2026"


# Home Page
@app.route('/')
def home():
    if 'student_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name'].strip()
        email = request.form['email'].strip().lower()
        password = request.form['password']
        course = request.form['course'].strip()

        if not name or not email or not password or not course:
            flash("All fields are required!", "error")
            return redirect(url_for('register'))

        if len(password) < 6:
            flash("Password must contain at least 6 characters!", "error")
            return redirect(url_for('register'))

        connection = get_connection()

        if connection:
            cursor = connection.cursor()

            try:
                hashed_password = generate_password_hash(password)

                cursor.execute("""
                    INSERT INTO students (name, email, password, course)
                    VALUES (%s, %s, %s, %s)
                """, (name, email, hashed_password, course))

                connection.commit()
                flash("Registration successful! Please login.", "success")
                return redirect(url_for('login'))

            except Exception:
                connection.rollback()
                flash("Email already registered or invalid details!", "error")

            finally:
                cursor.close()
                connection.close()

        else:
            flash("Database connection failed!", "error")

    return render_template('register.html')


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email'].strip().lower()
        password = request.form['password']

        connection = get_connection()

        if connection:
            cursor = connection.cursor()

            cursor.execute(
                "SELECT id, name, email, password, course FROM students WHERE email = %s",
                (email,)
            )

            student = cursor.fetchone()

            cursor.close()
            connection.close()

            if student and check_password_hash(student[3], password):
                session['student_id'] = student[0]
                session['student_name'] = student[1]
                session['student_email'] = student[2]
                session['student_course'] = student[4]

                return redirect(url_for('dashboard'))

            flash("Invalid email or password!", "error")

        else:
            flash("Database connection failed!", "error")

    return render_template('login.html')


# Dashboard Page
@app.route('/dashboard')
def dashboard():

    if 'student_id' not in session:
        return redirect(url_for('login'))

    return render_template(
        'dashboard.html',
        name=session['student_name'],
        email=session['student_email'],
        course=session['student_course']
    )


# Logout
@app.route('/logout')
def logout():

    session.clear()
    flash("You have logged out successfully!", "success")

    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)