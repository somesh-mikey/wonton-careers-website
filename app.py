from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

company_name = "Wonton"
jobs = [
    {"title": "Software Engineer", "location": "Remote", "salary": "$100,000"},
    {"title": "Data Scientist", "location": "New York, NY", "salary": "$50,000"},
    {"title": "Product Manager",
     "location": "San Francisco, CA", "salary": "$120,000"},
]


@app.route("/")
def home():
    return render_template("home.html", company_name=company_name, jobs=jobs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/courses")
def courses():
    return render_template("courses.html")


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
