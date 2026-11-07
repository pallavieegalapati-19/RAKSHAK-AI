from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

reports = []
events = []

def get_priority(category):
    c = category.lower()
    if "fire" in c or "medical" in c or "crowd" in c or "missing" in c:
        return "HIGH"
    return "MEDIUM"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/user", methods=["GET", "POST"])
def user_view():
    if request.method == "POST":
        category = request.form.get("category")
        reports.append({
            "name": request.form.get("name"),
            "phone": request.form.get("phone"),
            "category": category,
            "location": request.form.get("location"),
            "message": request.form.get("message"),
            "priority": get_priority(category),
            "time": datetime.now().strftime("%d-%m-%Y %H:%M")
        })
        return "<h2 style='text-align:center;margin-top:100px;'>✅ Report Sent Successfully! Police ki vellipoyindi!<br><br><a href='/'>Back to Home</a></h2>"
    return render_template("user.html")

@app.route("/report", methods=["POST"])
def report():
    return redirect("/user")

@app.route("/organizer", methods=["GET", "POST"])
def organizer_view():
    if request.method == "POST":
        events.append({
            "event_name": request.form.get("event_name"),
            "date_time": request.form.get("date_time"),
            "location": request.form.get("location"),
            "crowd": request.form.get("crowd"),
            "gates": request.form.get("gates"),
            "ambulance": request.form.get("ambulance"),
            "organizer_name": request.form.get("organizer_name"),
            "organizer_phone": request.form.get("organizer_phone")
        })
        return "<h2 style='text-align:center;margin-top:100px;'>✅ Event Saved! Police ki send ayyindi!<br><br><a href='/'>Back to Home</a></h2>"
    return render_template("organizer.html")
@app.route("/quick-sos")
def quick_sos():
    reports.append({
        "name": "Unknown - Emergency!",
        "phone": "Not Provided",
        "category": "EMERGENCY - Need Help NOW",
        "location": "Live Location - GPS Tracking",
        "message": "QUICK SOS - Person in danger, cannot fill form. Send help immediately!",
        "priority": "HIGH",
        "time": datetime.now().strftime("%d-%m-%Y %H:%M")
    })
    return "<h1 style='text-align:center; margin-top:100px; color:red;'>🚨 SOS SENT! HELP IS ON THE WAY!<br><br>Police ki location vellipoyindi!<br><br><a href='/'>Back to Home</a></h1>"
@app.route("/police")
def police_view():
    return render_template("police.html", reports=reports, events=events)

@app.route("/map")
def map_view():
    return render_template("map.html", reports=reports, events=events)

@app.route("/events")
def events_view():
    return render_template("events.html", events=events)

if __name__ == "__main__":
    app.run(debug=True)