import platform
from flask import Flask, render_template
from gevent.pywsgi import WSGIServer
import os, losses,export,serials,ghist,gnum
from old import users

db_server        = os.getenv("DB_HOST", '192.168.10.5')
db_port          = os.getenv("DB_PORT", 3053)
db_path          = os.getenv("DB_PATH", 'sklad_prod')
db_user          = os.getenv("DB_USER", 'MONITOR')
db_password      = os.getenv("DB_PASSWORD", 'inwino')
local_ip         = os.getenv('LOCAL_IP','192.168.10.9')
server_port      = os.getenv('SERVER_PORT',3001)

app = Flask(__name__)
app.secret_key = '435343ku4vjjq3eqhdeql3545345ts2cgvfkdc'  # потрібен для flash-повідомлень



########## MAIN ####################
@app.context_processor
def inject_globals():
    dsn = db_server + '/' + str(db_port) + ':' + db_path
    return {
        'version': 'v0.0.2.100',
        'appname': 'UkrSklad Addons App',
        'dsn': dsn
    }

@app.route('/')
def index():
    return render_template('index.html')

############# USERS ################
@app.route('/users')
def list_users():
    return users.list_users()

@app.route('/add', methods=['POST'])
def add_user():
    return users.add_user()

@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    return users.delete_user(user_id)

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(num):
    return users.edit_user(num)

############# LOSSES ######################################
@app.route('/losses', methods=['GET', 'POST'])
def losses_list():
    return losses.losses_list()

@app.route("/lost_add", methods=["GET", "POST"])
def loss_add():
    return losses.loss_add()
############ EXPORT ########################################
@app.route("/export")
def export_csv():
    return export.export_csv()

########### SERIAL#############################################
@app.route("/serials",methods=['GET', 'POST'])
def serials_search():
    return serials.serials_search()

########### G_HIST ############################################
@app.route("/ghist",methods =['GET','POST'])
def ghist_search():
    return ghist.search()

########### G_NUM #############################################
@app.route("/gnum",methods =['GET','POST'])
def gnum_search():
    return gnum.search()

############ TEST ##########################################
# @app.route("/test")
@app.route('/test/<int:record_id>', methods=['GET', 'POST'])
def edit_record(record_id):
    return test.edit_record(record_id)

@app.route('/users_pages')
def users_pages():
    return pages.list_users()

@app.route('/run_procedure', methods=["POST"])
def run_procedure():
    return '/run_procedure'
########### MAIN ##############################################
if __name__ == "__main__":
    if platform.system() == 'Windows':
        http_server = WSGIServer((local_ip, int(server_port)), app)
        print(f"Running HTTP-SERVER on port - http://" + local_ip + ':' + str(server_port))
    else:
        http_server = WSGIServer(('', int(server_port)), app)
        print(f"Running HTTP-SERVER on port :" + str(server_port))
    http_server.serve_forever()
