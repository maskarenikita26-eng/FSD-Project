from flask import Flask , request, render_template
import psycopg2

app = Flask(__name__)

# Connect to database
def db_connect():
    return psycopg2.connect(
        dbname = 'studentdb',
        user = 'postgres',
        password = 'Tanuja@1106',
        host = 'localhost',
        port = '5432'
    ) 

# Create Student table
def create_table():

    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Student1(
            student_id INT PRIMARY KEY,
            name VARCHAR(100),
            course VARCHAR(100)
            )
""")

    con.commit()
    cur.close()
    con.close()

# Student Registration
@app.route("/", methods = ['GET','POST'])
def register():

    msg = ""

    if request.method == "POST":
        sid = request.form['student_id'].strip()
        name = request.form['name'].strip()
        course = request.form['course'].strip()

        if sid == "" or name == "" or course == "":
            msg = "Please fill in all fields."
        else:
            con = db_connect()
            cur = con.cursor()

            cur.execute(
                "INSERT INTO Student (student_id, name, course) VALUES(%s,%s,%s)",(sid,name, course)
            )

            con.commit()
            cur.close()
            con.close()

            msg = "Student registered sucessfully!"

    return render_template("index.html", msg = msg)

if __name__ == '__main__':
    create_table()
    app.run(debug = True)
