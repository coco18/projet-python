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
    a = Activity()
    city = request.forms.city
    list_activity = a.select_list_in_city(DB, city)
    DB.deconnect()
    return template("web/city", city=city, list_activity= list_activity)

@route('/activity', method='GET')
def city():
    DB = Db()
    p = Place()
    activity = request.query.activity
    city = request.query.city
    list_equipment = p.select_place_of_activity_in_city(DB, activity, city)
    DB.deconnect()
    return template("web/activity", list_equipment=list_equipment)


@route('/equipement', method='GET')
def city():
    DB = Db()
    p = Place()
    idequipement = request.query.id
    e = DB.select_equipement(idequipement)
    place = p.select_place(DB, e.num_place)
    DB.deconnect()
    return template("web/equipement", equipement=e, place=place)


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
