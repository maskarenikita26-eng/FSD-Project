from flask import Flask, requests
app = Flask(__name__)
students = ["tanuja", "Rutuja","ankita","gayatri"]
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":

        name = request.form.get("name")

        if name in students:
            result = f"student found : {name}"
        else:
            result = f" student not found : {name}"

        return f"""
        <h2>Search Result </h2>
        <p>{result}</p>
      """
    return """
    <h2>Student Search</h2>
    <form method="POST">
        Name:
        <input type="text" name="name">
        <br><br>
        <input type="submit" value="Search">
    </form>
    """
app.run(debug=True)