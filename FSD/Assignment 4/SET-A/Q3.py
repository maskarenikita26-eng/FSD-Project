from flask import Flask
app=Flask(__name__)

@app.route('/course/<name>')
def course(name):
    
     return f"welcome to {name} page"
if __name__=='__main__':
     app.run(debug=True)