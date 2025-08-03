from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Приклад даних
rows = [
    {"ID": 1, "NAME": "Авто 1", "STATUS": "Активний"},
    {"ID": 2, "NAME": "Авто 2", "STATUS": "Очікує"},
    {"ID": 3, "NAME": "Авто 3", "STATUS": "Неактивний"},
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        row_id = int(request.form["ID"])
        for row in rows:
            if row["ID"] == row_id:
                row["NAME"] = request.form["NAME"]
                row["STATUS"] = request.form["STATUS"]
        return redirect(url_for("index"))

    return render_template("modal_edit.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True,port=5001)
