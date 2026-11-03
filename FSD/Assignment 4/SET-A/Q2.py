from flask import Flask
app=Flask(__name__)

@app.route('/contact')
def contact():
    return "Welcome to conatact  our page"


@app.route('/services')
def services():
    return "this is service page"
if __name__ =='__main__':
    app.run(debug=True)