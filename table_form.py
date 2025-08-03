from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Дані — просто масив словників
cars = [
    {"id": 1, "brand": "Toyota", "model": "Corolla"},
    {"id": 2, "brand": "Honda", "model": "Civic"},
    {"id": 3, "brand": "Ford", "model": "Focus"}
]

@app.route('/')
def index():
    edit_id = request.args.get('edit_id', type=int)
    car_to_edit = next((car for car in cars if car["id"] == edit_id), None)
    return render_template("table_form.html", cars=cars, edit_car=car_to_edit)

@app.route('/update', methods=['POST'])
def update():
    car_id = int(request.form['id'])
    brand = request.form['brand']
    model = request.form['model']

    for car in cars:
        if car["id"] == car_id:
            car["brand"] = brand
            car["model"] = model
            break

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
