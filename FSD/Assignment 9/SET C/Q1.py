from flask import Flask, request, render_template, redirect
import psycopg2
app = Flask(__name__)
def db_connect():
    return psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="Tanuja@1106",
        host="localhost",
        port="5432")
def create_table():
    con = db_connect()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Student (
            Student_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Course VARCHAR(100))
    """)
    con.commit()
    cur.close()
    con.close()
@app.route("/", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        con = db_connect()
        cur = con.cursor()
        name = request.form["Name"]
        course = request.form["Course"]
        cur.execute(
            "INSERT INTO Student (Name, Course) VALUES (%s, %s)",
            (name, course))
        con.commit()
        cur.close()
        con.close()
        return redirect("/display")
    return render_template("add.html")
@app.route("/display")
def display_students():
    con = db_connect()
    cur = con.cursor()
    cur.execute("SELECT * FROM Student ORDER BY Student_ID")
    students = cur.fetchall()
    cur.close()
    con.close()
    return render_template("display.html", students=students)
@app.route("/update", methods=["GET", "POST"])
def update_student():
    if request.method == "POST":
        con = db_connect()
        cur = con.cursor()
        sid = request.form["Student_ID"]
        name = request.form["Name"]
        course = request.form["Course"]
        cur.execute(
            "UPDATE Student SET Name=%s, Course=%s WHERE Student_ID=%s",
            (name, course, sid)
        )
        con.commit()
        cur.close()
        con.close()
        return redirect("/display")
    return render_template("update.html")
@app.route("/delete", methods=["GET", "POST"])
def delete_student():
    if request.method == "POST":
        sid = request.form["Student_ID"]
        con = db_connect()
        cur = con.cursor()
        cur.execute(
            "DELETE FROM Student WHERE Student_ID=%s",
            (sid,)
        )
        con.commit()
        cur.close()
        con.close()
        return redirect("/display")
    return render_template("delete.html")
if __name__ == "__main__":
    create_table()
    app.run(debug=True)

