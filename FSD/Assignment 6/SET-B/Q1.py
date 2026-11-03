from flask import Flask,jsonify

app=Flask(__name__)

@app.route("/student" , methods=['GET'])
def student():
    student1={
        "name":"pardhi tanuja",
        "age":20,
        "roll_no":48
    }
    student2={
            "name":"shelar ankita",
            "age":20,
            "roll_no":57
    }
    

    return jsonify(student1,student2)
if __name__=='__main__':
    app.run(debug=True)
    

    

