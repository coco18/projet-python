from bottle import get, post, request, run, route, static_file, template
from db import Db

@route('/')
def index():
    DB = Db()
    data=DB.select_list_activity()
    data_city = DB.select_list_city()
    return template("web/index", data=data, data_city =data_city)

@route('/city', method='POST')
def city():
    DB = Db()
    city = request.forms.city
    list_activity = DB.select_list_activity_in_city(city)
    return template("web/city", city=city, list_activity= list_activity)

@route('/activity', method='GET')
def city():
    DB = Db()
    activity = request.query.activity
    city = request.query.city
    list_equipement = DB.select_place_of_activity_in_city(activity, city)
    return template("web/activity", list_equipement=list_equipement)


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
