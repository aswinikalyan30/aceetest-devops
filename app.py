from flask import Flask, render_template, request, redirect
from database import init_db, get_connection

app = Flask(__name__)

init_db()


@app.route("/")
def index():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM clients")
    clients = cur.fetchall()

    conn.close()

    return render_template("index.html", clients=clients)


@app.route("/add_client", methods=["POST"])
def add_client():

    name = request.form["name"]
    age = request.form["age"]
    height = request.form["height"]
    weight = request.form["weight"]
    program = request.form["program"]

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO clients(name,age,height,weight,program) VALUES(?,?,?,?,?)",
        (name, age, height, weight, program)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/add_workout", methods=["POST"])
def add_workout():

    client = request.form["client"]
    date = request.form["date"]
    workout = request.form["workout"]
    duration = request.form["duration"]

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO workouts(client_name,date,workout_type,duration) VALUES(?,?,?,?)",
        (client, date, workout, duration)
    )

    conn.commit()
    conn.close()

    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)