from flask import  request,render_template
import db


def search():
    result = []
    search_term = ''
    if request.method == 'POST':
        sql = "select * from monitoring.get_serials_by_tov_sklad(?)"
        serial = request.form.get('serial', '').strip()
        # result = db.get_data(sql, [tov_id])
        # total = len(result)
        # sql = "select tn.name from tovar_name tn where tn.num = ?"
        # tov_name = db.get_data(sql, [tov_id], 1)
        return render_template('g_hist.html',  title='Історія товару', serial=serial,
                            )

    return render_template('g_hist.html', result=None, title='Історія товару', total=None, tov_name=None)