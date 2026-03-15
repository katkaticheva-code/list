from flask import Flask, render_template, request, redirect

app = Flask(__name__)

events = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        date = request.form["date"]
        time = request.form["time"]
        priority = request.form["priority"]

        event = {
            "name": name,
            "date": date,
            "time": time,
            "priority": priority
        }

        events.append(event)

        return redirect("/")

    return render_template("index.html", events=events)


@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(events):
        events.pop(index)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)