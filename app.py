from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/cal")
def calendar():
    return render_template('calendar.html')

@app.route("/children")
def children():
    return render_template('children.html')

@app.route("/rewards")
def rewards():
    return render_template('rewards.html')

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port='8000')