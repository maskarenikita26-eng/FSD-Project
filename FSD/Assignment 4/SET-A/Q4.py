from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "wlcome to home page"

@app.route('/student')
def student():
    return "This is student page"

@app.route('/faculty')
def faculty():
    return "Welcome to faculty page"

if __name__=='__main__':
    app.run(debug=True)