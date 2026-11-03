from flask import Flask, request, render_template
import psycopg2
app = Flask(__name__)
def get_connect():
    con = psycopg2.connect(
        dbname="employeedb",
        user="postgres",
        password="Tanuja@1106",
        host="localhost",
        port="5432"
    )
    return con
def create_table():
    con = get_connect()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Employeedb (
            Emp_ID SERIAL PRIMARY KEY,
            Name VARCHAR(100),
            Department VARCHAR(100)
        );
    """)
    con.commit()
    cur.close()
    con.close()
@app.route("/employee", methods=["GET", "POST"])
def employee():
    con = get_connect()
    cur = con.cursor()
    if request.method == "POST":
        name = request.form.get("Name")
        department = request.form.get("Department")
        cur.execute(
            "INSERT INTO Employeedb (Name, Department) VALUES (%s, %s)",
            (name, department)
        )
        con.commit()
    cur.execute("SELECT * FROM Employeedb ORDER BY Emp_ID")
    employees = cur.fetchall()
    cur.close()
    con.close()
    return render_template("employee.html", employees=employees)
if __name__ == "__main__":
    create_table()
    app.run(debug=True)
