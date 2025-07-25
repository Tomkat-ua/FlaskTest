from flask import  request,render_template
import db


def search():
    result = []
    search_term = ''
    print(request.method)
    title = 'Історія товару'
    if request.method == 'POST':
        # user_data = {
        #     "Ім’я": "Олександр",
        #     "Email": "olex@example.com",
        #     "Телефон": "+380 50 123 4567",
        #     "Роль": "Адміністратор"
        # }

        sql = ("select distinct  ts.tovar_id, ts.tovar_ser_num ,tn.name "
               " from tovar_serials ts "
               " inner join tovar_name tn on tn.num = ts.tovar_id "
               " where ts.tovar_ser_num like (?)")
        tov_serial = request.form.get('tov_serial', '').strip()
        print('tov_serial',tov_serial)
        records = db.get_data(sql, [tov_serial])
        if records:
            record = records[0]
            print(record)
            fields = {
                "F1": record[0],
                "F2": record[1],
                "F3": record[2]
            }
            print('data',fields)
            return render_template('ghist.html',title=title,data=fields,serial="Знайдено дані для "+ tov_serial)
        else:
            return render_template('ghist.html',title=title,data=None ,serial="НЕ знайдено дані для " + tov_serial)

    return render_template('ghist.html', title=title, tov_name=None, serial=None)