from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/<station>/<date>")
def access(station, date):
    temperature = 1
    return {"station": station,
            "date": date,
            "temperature": temperature}


app.run(debug=True)
