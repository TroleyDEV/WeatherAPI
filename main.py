from flask import Flask, render_template

app = Flask(__name__)


# Create home page
@app.route("/")
def home():
    return render_template("index.html")


# Create API page
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


# Run app
if __name__ == "__main__":
    app.run(debug=True)
