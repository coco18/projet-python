from bottle import get, post, request, run, route, static_file, template
from db import Db
from activity import Activity
from place import Place
from equipment import Equipment

@route('/')
def index():
    DB = Db()
    a = Activity()
    p = Place()
    data=a.select_list(DB)
    data_city = p.select_list_city(DB)
    DB.deconnect()
    return template("web/index", data=data, data_city =data_city)

@route('/city', method='POST')
def city():
    DB = Db()
    a = Activity()
    city = request.forms.city
    list_activity = a.select_list_in_city(DB, city)
    DB.deconnect()
    return template("web/city", city=city, list_activity= list_activity)

@route('/activity', method='GET')
def city():
    DB = Db()
    e = Equipment()
    activity = request.query.activity
    city = request.query.city
    list_equipment = e.select_place_of_activity_in_city(DB, activity, city)
    DB.deconnect()
    return template("web/activity", list_equipment=list_equipment)


@route('/equipment', method='GET')
def city():
    DB = Db()
    p = Place()
    idequipment = request.query.id
    e = Equipment().select(DB,idequipment)
    place = p.select_place(DB, e.num_place)
    DB.deconnect()
    return template("web/equipment", equipment=e, place=place)


@route('/search', method='GET')
def default():
    DB = Db()
    act = request.query.activity
    data=Equipment().search(DB,"'"+act+"'")
    return template("web/resultat_recherche.tpl",data = data)

@route('/search2', method='Post')
def default():
    DB = Db()
    eq = request.query.equipment
    act = request.query.activity
    data=Equipment().select_place_of_activity_in_city(DB,"'"+eq+"'")
    return template("web/resultat.tpl",data = data)

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
