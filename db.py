import main, fdb,platform


def get_connection():
    if platform.system() == 'Windows':
        return fdb.connect(
            # dsn='192.168.10.9/3053:D:/data/database1.fdb',
            # dsn = '192.168.10.5/3053:sklad_dev',
            host=main.db_server,
            port=main.db_port,
            database=main.db_path,
            user=main.db_user,
            password=main.db_password,
            fb_library_name="C:/sklad/x64/fbclient.dll",
            charset="utf-8"
        )
    else:
        return fdb.connect(
            host=main.db_server,
            port=main.db_port,
            database=main.db_path,
            user=main.db_user,
            password=main.db_password,
            charset="utf-8"
        )

def get_data(sql,params,mode=1):
    con = get_connection()
    cur = con.cursor()
    cur.execute(sql,params)
    result  = ''
    try:
        if mode == 1:
            result = cur.fetchall()
        if mode == 2:
            result = cur.fetchone()
    except Exception as e:
        print(str(e))
    con.close()
    return result
