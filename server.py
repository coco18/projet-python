from web.bottle import get, post, request, run, route, static_file, template
from db.db import Db
from model.activity import Activity
from model.place import Place
from model.equipment import Equipment

@route('/')
def index():
    """Display the welcome page"""
    DB = Db()
    a = Activity()
    p = Place()
    data=a.select_list(DB)
    data_city = p.select_list_city(DB)
    DB.deconnect()
    return template("web/index", data=data, data_city =data_city)

@route('/city', method='POST')
def city():
    """Display the page who contains the list of the activities in a city """
    DB = Db()
    a = Activity()
    city = request.forms.city
    list_activity = a.select_list_in_city(DB, city)
    DB.deconnect()
    return template("web/city", city=city, list_activity= list_activity)

@route('/activity', method='GET')
def city():
    """Display the page who contains the list of the equipment """
    DB = Db()
    e = Equipment()
    id_activity = request.query.activity
    city = request.query.city
    list_equipment = e.select_place_of_activity_in_city(DB, id_activity, city)
    activity = Activity()
    activity.select(DB, id_activity)
    DB.deconnect()
    return template("web/activity", acivity=activity, city=city, list_equipment=list_equipment)


@route('/equipment', method='GET')
def city():
    """Display the page who display an equipment """
    DB = Db()
    e = Equipment()
    p = Place()
    idequipement = request.query.id
    e.select(DB, idequipement)
    place = p.select(DB, e.num_place)
    DB.deconnect()
    return template("web/equipment", equipment=e, place=place)


@route('/search', method='GET')
def default():
    """Display the page who display the list of the equipment for an activity  """
    DB = Db()
    act = request.query.activity
    list_equipment=Equipment().search(DB,"'"+act+"'")
    DB.deconnect()
    return template("web/resultat_recherche.tpl", act=act, list_equipment = list_equipment)

@route('/<filepath:path>')
def server_static(filepath):
    """Root to the repertory web """
    return static_file(filepath, root='./web/')

@route("/css/<filename>")
def style(filename):
    """Root to the repertory web/ccs """
    return static_file(filename, root='web/css/')

@route("/images/<filename>")
def img(filename):
    """Root to the repertory web/img """
    return static_file(filename,root="web/img/")

@route("/js/<filename>")
def script(filename):
    """Root to the repertory web/js """
    return static_file(filename, root='web/js/')

run(host='localhost', port=8081, debug=True)
