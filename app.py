from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/cal")
def calendar():
    return render_template('calendar.html')

@app.route("/children", methods=['POST', 'GET'])
def children():
    if request.method == "POST":
        fn = request.form["fn"]
        ln = request.form["ln"]
        age = request.form["age"]
        return render_template("children.html", first_name=fn, last_name=ln, age=age)
    else:
        return render_template("student_forms.html")

@app.route("/rewards")
def rewards():
    return render_template('rewards.html')


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port='8000')