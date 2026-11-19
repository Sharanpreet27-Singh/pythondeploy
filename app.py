import csv, os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from data import SERVICES, PLANS, TRAINERS, SUPPLEMENTS

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-me-in-production")
MESSAGES_FILE = os.path.join(os.path.dirname(__file__), "messages.csv")


@app.context_processor
def inject_globals():
    return {"gym_name": "IronNest Fitness", "year": datetime.now().year}


@app.route("/")
def home():
    return render_template("index.html", services=SERVICES[:6], plans=PLANS,
                           trainers=TRAINERS, supplements=SUPPLEMENTS[:4])


@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES, trainers=TRAINERS)


@app.route("/supplements")
def supplements():
    categories = ["All"] + sorted({s["category"] for s in SUPPLEMENTS})
    selected = request.args.get("category", "All")
    items = SUPPLEMENTS if selected == "All" else [s for s in SUPPLEMENTS if s["category"] == selected]
    return render_template("supplements.html", items=items, categories=categories, selected=selected)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        message = request.form.get("message", "").strip()
        if not (name and phone and message):
            flash("Please fill in your name, phone number and message.", "error")
            return render_template("contact.html", form=request.form)
        with open(MESSAGES_FILE, "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([datetime.now().isoformat(), name, phone, message])
        flash("Thanks, we received your message and will call you within a day.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", form={})


@app.errorhandler(404)
def not_found(_):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", port=int(os.environ.get("PORT", 5000)))
