import sqlite3

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
        cur.execute("DROP TABLE IF EXISTS equipementactivity")
        cur.execute("CREATE TABLE equipementactivity(id_equipement integer, id_activity integer, PRIMARY KEY (id_equipement,id_activity), FOREIGN KEY(id_equipement) REFERENCES equipement(id), FOREIGN KEY(id_activity) REFERENCES activity(id))")

    def insert_in_place(self, place):
        c = self.con.cursor()
        insert_query = "INSERT INTO place(id, name_place, num_street, street, place_says, city, city_code, longitude, latitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        c.execute(insert_query, (place.id, place.name_place, place.num_street, place.street, place.place_says, place.city, place.city_code, place.longitude, place.latitude))


    def insert_in_equipement(self, equipement):
        c = self.con.cursor()
        insert_query = "INSERT INTO equipement(id, name_equipement, num_place) VALUES (?, ?, ?)"
        c.execute(insert_query, (equipement.id, equipement.name_equipement, equipement.num_place))


    def insert_in_activity(self, activity):
        c = self.con.cursor()
        insert_query = "INSERT INTO activity(id, name_activity, level_activity) VALUES (?, ?, ?)"
        c.execute(insert_query, (activity.id, activity.name_activity, activity.level_activity))

    def insert_in_equipement_activity(self, equipementactivity):
        c = self.con.cursor()
        insert_query = "INSERT INTO equipementactivity(id_equipement, id_activity) VALUES (?, ?)"
        c.execute(insert_query, (equipementactivity.id_equipement, equipementactivity.id_activity))

    def activity_exist(self, num_activity):
        c = self.con.cursor()
        insert_query = "SELECT id FROM activity WHERE id=(?)"
        c.execute(insert_query, (num_activity,))
        tmp=None
        for row in c:
            tmp = row[0]
        if tmp==int(num_activity):
            return True
        else:
            return False

    def equipementactivity_exist(self, num_equipement, num_activity):
        c = self.con.cursor()
        insert_query = "SELECT id_activity FROM equipementactivity WHERE id_equipement=(?)"
        c.execute(insert_query, (num_equipement,))
        tmp=None
        exist=False
        for row in c:
            tmp = row[0]
            if tmp==int(num_activity):
                exist=True
        if exist:
            return True
        else:
            return False

    def search(self,table,genre,texte): #mettre texte entre "''"
        c = self.con.cursor()
        query =  "SELECT * FROM {0} where {1} LIKE {2}".format(table, genre, texte)
        c.execute(query)
        return c.fetchall()

    def searchequipement(self,texte):
        c = self.con.cursor()
        query = "SELECT name_equipement from equipement where id IN (SELECT id_equipement from equipementactivity where id_activity in (SELECT id FROM activity  where name_activity = {0}))".format(texte)
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

    def select_list_activity(self):
        c = self.con.cursor()
        query =  "SELECT name_activity FROM activity "
        c.execute(query)
        tab=[]
        for row in c.fetchall():
            tab.append(row[0])
        tab.sort()
        return tab

    def commit(self):
        self.con.commit()

    def deconnect(self):
        self.con.close()
