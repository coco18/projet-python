from bottle import get, post, request, run, route, static_file, template
from db import Db

@route('/')
def index():
    DB = Db()
    data=DB.select_list_activity()
    return template("web/index", data=data)

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
