from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def invitation():
    return render_template("index.html")

@app.route("/venue")
def venue():
    return render_template("venue.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

if __name__ == "__main__":
    app.run(debug=True)
