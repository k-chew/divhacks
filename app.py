from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "much secret lel"

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/cal")
def calendar():
    return render_template('calendar.html')

@app.route("/children", methods=['POST', 'GET'])
def children():
    if request.method == "POST":
        session["fn"] = request.form["fn"]
        session["ln"] = request.form["ln"]
        session["age"] = request.form["age"]
        session["number"] = request.form["selection"]
        for i in range(1, int(session["number"]) + 1):
            session[str(i)] = request.form.get(str(i-1))
            print(request.form.get(str(i)))
        return render_template("children.html", first_name=session["fn"], last_name=session["ln"], age=session["age"])
    else:
        return render_template("student_forms.html")

@app.route("/rewards")
def rewards():
    return render_template('rewards.html')


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port='8000')