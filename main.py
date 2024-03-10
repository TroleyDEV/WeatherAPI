import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

stations = pd.read_csv("data/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


# Create home page
@app.route("/")
def home():
    return render_template("index.html", data=stations.to_html())


# Create API page
@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # Get dataframe for specific station
    df = pd.read_csv(f"data/TG_STAID{str(station).zfill(6)}.txt", skiprows=20, parse_dates=["    DATE"])
    # Get temperature for specific date and station
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


# Run app
if __name__ == "__main__":
    app.run(debug=True)
