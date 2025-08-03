import db
from flask import  request, redirect, flash,render_template

def list_users():
    query = request.args.get('q', '')
    con = db.get_connection()
    cur = con.cursor()
    if query:
        like_query = f"%{query}%"
        cur.execute("SELECT * FROM s_users WHERE u_login LIKE ? OR u_login LIKE ?", (like_query, like_query))
    else:
        cur.execute("SELECT * FROM s_users")
    users = cur.fetchall()
    con.close()
    return render_template('users.html', users=users,title = 'Користувачі')


def add_user():
    login = request.form['login']
    name = request.form['name']
    con = db.get_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO s_users (u_login, u_login) VALUES (?, ?)", (login, name))
    con.commit()
    con.close()
    flash(f'Користувача "{login}" додано успішно.')
    return redirect('/')

def delete_user(user_id):
    con = db.get_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE id=?", (user_id,))
    con.commit()
    con.close()
    flash(f'Користувача з ID {user_id} видалено.')
    return redirect('/')

def edit_user(num):
    con = db.get_connection()
    cur = con.cursor()
    if request.method == 'POST':
        login = request.form['login']
        name = request.form['name']
        cur.execute("UPDATE s_users SET u_login=?, u_name=? WHERE num=?", (login, name, num))
        con.commit()
        flash(f'Користувача #{num} оновлено.')
        con.close()
        return redirect('/')
    else:
        cur.execute("SELECT * FROM s_users WHERE num=?", (num,))
        user = cur.fetchone()
        con.close()
        if not user:
            flash("Користувача не знайдено.")
            return redirect('/')
        return render_template('user_edit.html', user=user)