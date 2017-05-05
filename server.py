from bottle import get, post, request, run, route, static_file, template
from db import Db

@route('/')
def index():
    DB = Db()
    data=DB.select_list_activity()
    return template("web/index", data=data)

@route('/search', method='GET')
def default():
    DB = Db()
    if(request.query.activity) :
        act = request.query.activity
        data=DB.searchequipement("'"+act+"'")
        return template("web/resultat_recherche.tpl",data = data)
    #creer un get equipement ! pour fournir l'adresse
    return "bouhouhou"

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./web/')

@route("/css/<filename>")
def style(filename):
    return static_file(filename, root='web/css/')

@route("/img/<filename>")
def img(filename):
	return static_file(filename,root="web/img/")

@route("/js/<filename>")
def script(filename):
    return static_file(filename, root='web/js/')

run(host='localhost', port=8081, debug=True)
