import sqlite3
import locale
from activity import Activity
from place import Place
from equipement import Equipement

class Db:
    """docstring for data base"""
    def __init__(self):
        self.con = sqlite3.connect("data.db")

    def create_table(self):
        cur = self.con.cursor()
        cur.execute("DROP TABLE IF EXISTS place")
        cur.execute("CREATE TABLE place(id integer PRIMARY KEY, name_place text, num_street integer, street text, place_says text, city text, city_code integer, longitude integer, latitude integer)")
        cur.execute("DROP TABLE IF EXISTS equipement")
        cur.execute("CREATE TABLE equipement(id integer PRIMARY KEY, name_equipement text, num_place integer, FOREIGN KEY(num_place) REFERENCES place(id))")
        cur.execute("DROP TABLE IF EXISTS activity")
        cur.execute("CREATE TABLE activity(id integer PRIMARY KEY, name_activity text, level_activity text)")
        cur.execute("DROP TABLE IF EXISTS equipmentactivity")
        cur.execute("CREATE TABLE equipmentactivity(id_equipment integer, id_activity integer, PRIMARY KEY (id_equipment,id_activity), FOREIGN KEY(id_equipment) REFERENCES equipment(id), FOREIGN KEY(id_activity) REFERENCES activity(id))")


    def search(self,table,genre,texte): #mettre texte entre "''"
        c = self.con.cursor()
        query =  "SELECT * FROM {0} where {1} LIKE {2}".format(table, genre, texte)
        c.execute(query)
        return c.fetchall()

    def searchcity(self,activity,equipement):
        c = self.con.cursor()
        query = "SELECT * from place where id in (SELECT num_place from equipement where name_equipement= {1} and id IN (SELECT id_equipement from equipementactivity where id_activity in (SELECT id FROM activity  where name_activity = {0})))".format(activity,equipement)
        c.execute(query)
        return c.fetchall()

    def displaytable(self,table):
        c = self.con.cursor()
        query =  "SELECT * FROM {0} ".format(table)
        c.execute(query)
        return c.fetchall()



    def select_list_city(self):
        c = self.con.cursor()
        query =  "SELECT city FROM place "
        c.execute(query)
        tab=[]
        for row in c.fetchall():
            tab.append(row[0])
        tab = set(tab)
        locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")
        x = [a for a in sorted(tab, key=locale.strxfrm)]
        return x



<<<<<<< HEAD
    def select_num_place(self, city):
        c = self.con.self)
        return tab

    def select_place(self, num_place):
        c = self.con.cursor()
        query = "SELECT * FROM place WHERE id={0} ".format(num_place)
        c.execute(query)
        p = Place()
        row = c.fetchone()
        p.id = row[0]
        p.name_place = row[1]
        p.num_street = row[2]
        p.street = row[3]
        p.place_says = row[4]
        p.city = row[5]
        p.city_code = row[6]
        p.longitude = row[7]
        p.latitude = row[8]
        return p


=======
>>>>>>> 13f926ac970abdfdc2f9002e26ea7b900dd18245
    def select_place_of_activity_in_city(self, activity, city):
        c = self.con.cursor()
        tab=[]
        num_place = list(self.select_num_place(city))
        for val in num_place:
            query = "SELECT * FROM equipement WHERE num_place ={1} and id in(SELECT id_equipement FROM equipementactivity WHERE id_activity in(SELECT id FROM activity WHERE id={0}))".format(str(activity), val)
            c.execute(query)
            for row in c.fetchall():
                e = Equipement()
                e.id = row[0]
                e.name_equipement = row[1]
                e.num_place = row[2]
                tab.append(e)
        return tab

    def commit(self):
        self.con.commit()

    def deconnect(self):
        self.con.close()
