from flask import Flask, render_template, request

app = Flask(__name__)

# Тестові дані
rows = [
    {'ID': 1, 'NAME': 'Авто 1', 'STATUS': 'Активний'},
    {'ID': 2, 'NAME': 'Авто 2', 'STATUS': 'Очікує'},
    {'ID': 3, 'NAME': 'Авто 3', 'STATUS': 'Неактивний'},
]

@app.route('/')
def index():
    selected_id = request.args.get('id', type=int)
    return render_template('table.html', rows=rows, selected_id=selected_id)

if __name__ == '__main__':
    app.run(debug=True)
