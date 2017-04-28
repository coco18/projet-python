from bottle import get, post, request, run, route, static_file

@route('web/<name>')
def index(name):
    return index('index', name=name)

run(host='localhost', port=8081)

@route("/css/<filename>")
def style(filename):
    return static_file(filename, root='web/css/')

@route("/img/<filename>")
def img(filename):
	return static_file(filename,root="web/img/")

@route("/js/<filename>")
def script(filename):
    return static_file(filename, root='web/js/')
