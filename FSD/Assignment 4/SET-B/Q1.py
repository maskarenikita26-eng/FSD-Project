from flask import Flask
app=Flask(__name__)

@app.route('/student/<name>')
def student(name):
 
    return f"welcome {name} in our page"



if __name__=='__main__':
    app.run(debug=True)