from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

registrations = []


@app.route("/")
def home():
    return render_template("index.html", registrations=registrations)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    event = request.form.get("event")

    if name and email and phone and event:
        registrations.append({
            "name": name,
            "email": email,
            "phone": phone,
            "event": event
        })

    return redirect(url_for("home"))


@app.route("/registrations")
def view_registrations():
    return render_template(
        "registrations.html",
        registrations=registrations
    )


if __name__ == "__main__":
    app.run(debug=True)