from flask import Flask, render_template

app = Flask("Website")

# Create page
@app.route("/home")
def home():
    return render_template("index.html")

# Run app
app.run(debug=True)
