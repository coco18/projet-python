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
        cur.execute("CREATE TABLE equipementactivity(id_equipement integer PRIMARY KEY, id_activity integer, FOREIGN KEY(id_equipement) REFERENCES equipement(id), FOREIGN KEY(id_activity) REFERENCES activity(id))")
        self.con.commit()

    def insert_in_place(self, place):
        c = self.con.cursor()

        insert_query = "INSERT INTO place(id, name_place, num_street, street, place_says, city, city_code, longitude, latitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        c.execute(insert_query, (place.id, place.name_place, place.num_street, place.street, place.place_says, place.city, place.city_code, place.longitude, place.latitude))
        self.con.commit()


    def insert_in_equipement(self, equipement):
        c = self.con.cursor()
        insert_query = "INSERT INTO equipement(id, name_equipement, num_place) VALUES (?, ?, ?)"
        c.execute(insert_query, (equipement.id, equipement.name_equipement, equipement.num_place))
        self.con.commit()


    def insert_in_activity(self, activity):
        c = self.con.cursor()

        insert_query = "INSERT INTO equipement(id, name_equipement, num_place) VALUES (?, ?, ?)"
        c.execute(insert_query, (activity.id, activity.name_equipement, activity.num_place))
        self.con.commit()

    def insert_in_equipement_activity(self, equipementactivity):
        c = self.con.cursor()
        insert_query = "INSERT INTO equipementactivity(id_equipement, id_activity) VALUES (?, ?)"
        c.execute(insert_query, (equipementactivity.id_equipement, equipementactivity.id_activity))
        self.con.commit()


    def deconnect(self):
        self.con.close()
