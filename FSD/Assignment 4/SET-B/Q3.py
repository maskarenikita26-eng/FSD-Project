from flask import Flask
app=Flask(__name__)

@app.route("/employee")
def employee():
    return "Welcome to employee page"
@app.route("/department")
def department():
    return "Welcome to department page"

@app.route("/contact")
def contact():
    return "This is contact page"

if __name__ =="__main__":
    app.run(debug=True)