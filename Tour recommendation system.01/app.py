from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# Recommendation page
@app.route("/recommend")
def recommend():
    return render_template("recommend.html")

# Result page (POST request)
@app.route("/result", methods=["POST"])
def result():

    place = request.form["place"]

    # sample data
    destinations = [
        {"name":"Goa","image":"goa.jpg"},
        {"name":"Manali","image":"manali.jpg"},
        {"name":"Darjeeling","image":"darjeeling.jpg"},
        {"name":"Jaipur","image":"jaipur.jpg"}
    ]

    return render_template("result.html", recs=destinations)

if __name__ == "__main__":
    app.run(debug=True)