from flask import Flask, request, render_template
import main,db
app = Flask(__name__)


def list_users():
    page = int(request.args.get('page', 1))
    per_page = 3
    offset = (page - 1) * per_page

    conn = db.get_connection()
    cur = conn.cursor()

    # 🔸 Підрахунок загальної кількості
    cur.execute("SELECT COUNT(*) FROM users")
    total_records = cur.fetchone()[0]
    total_pages = (total_records + per_page - 1) // per_page

    # 🔸 Пагінований запит
    cur.execute("""
        SELECT id, name, email FROM users
        ORDER BY id
        ROWS ? TO ?
    """, (offset + 1, offset + per_page))  # Firebird використовує ROWS x TO y

    users = cur.fetchall()

    return render_template(
        'users.html',
        users=users,
        page=page,
        total_pages=total_pages
    )
