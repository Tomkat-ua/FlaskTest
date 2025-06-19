import db
from flask import  request, redirect,render_template,url_for



def edit_record(record_id):
    con = db.get_connection()
    cur = con.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age'] or None
        gender = request.form['gender']
        country = request.form['country']
        note = request.form['note']

        cur.execute("""
            UPDATE users
            SET name = ?, email = ?, age = ?, gender = ?, country = ?, note = ?
            WHERE id = ?
        """, (name, email, age, gender, country, note, record_id))
        con.commit()
        return redirect(url_for('edit_record', record_id=record_id))

    # GET-запит — отримати існуючі дані
    cur.execute("SELECT name, email, age, gender, country, note FROM users WHERE id = ?", (record_id,))
    row = cur.fetchone()

    if row:
        record = {
            'id': record_id,
            'name': row[0],
            'email': row[1],
            'age': row[2],
            'gender': row[3],
            'country': row[4],
            'note': row[5],
        }
    else:
        record = None
    return render_template('edit_form.html', record=record)