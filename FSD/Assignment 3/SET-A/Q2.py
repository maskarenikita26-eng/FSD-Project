from flask import Flask
app = Flask(__name__) 
@app.route('/')
def home():
    return """
     <h1>Name:Tanuja Pardhi</h1>
     <h2>Roll No: 48</h2> """

if  __name__ == '__main__': 
    app.run(debug=True)
