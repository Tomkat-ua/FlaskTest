import db
from flask import  request, redirect, flash,render_template

def search():
    result = []
    search_term = ''
    print(request.method)
    if request.method == 'POST':
        sql = """ select  tn.name,ts.tovar_ser_num ,pd.tov_cena
                    from tovar_name tn
                     inner join tovar_serials ts on ts.tovar_id = tn.num and ts.doc_type_id =8
                     inner join pnakl  p  on p.num  = ts.doc_id
                     inner join pnakl_ pd on pd.pid = p.num and pd.tovar_id = ts.tovar_id
                    where upper(tn.name) like upper(?)  or ts.tovar_ser_num like ? """

        tov_serial = request.form.get('tov_serial', '').strip()
        tov_name = request.form.get('tov_name', '').strip()
        # keyword = request.form.get('keyword', '').strip()
        search_term = tov_name +  tov_serial
        result = db.get_data(sql, [tov_name,tov_serial])

        # total = len(result)
        # sql = "select tn.name from tovar_name tn where tn.num = ?"
        # tov_name = db.get_data(sql, [tov_id], 1)

        return render_template('gnum.html',  title='Пошук номерного товару', result=result,search_term=search_term)
    return render_template('gnum.html', result=None, title='Пошук номерного товару', total=None, tov_name=None)