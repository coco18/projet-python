import locale

class Place:
    """docstring for """
    def __init__(self):
        self.id = None
        self.name_place = None
        self.num_street = None
        self.street = None
        self.place_says = None
        self.city = None
        self.city_code = None
        self.longitude = None
        self.latitude = None


    """docstring for place"""
    def create_object(self, tab):
        self.id = tab[1]
        self.name_place = tab[0]
        self.num_street = tab[6]
        self.street = tab[7]
        self.place_says = tab[5]
        self.city = tab[2]
        self.city_code = tab[4]
        self.longitude = tab[9]
        self.latitude = tab[10]

    """select for place"""
    def select(self, db, num_place):
        c = db.con.cursor()
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

    def select_id_by_city(self, db, city):
        c = db.con.cursor()
        lcity = "'"+city+"'"
        query = "SELECT id FROM place WHERE city={0} ".format(lcity)
        c.execute(query)
        tab=[]
        for row in c.fetchall():
            tab.append(row[0])
        tab = set(tab)
        return tab

    def insert(self, db):
        c = db.con.cursor()
        insert_query = "INSERT INTO place(id, name_place, num_street, street, place_says, city, city_code, longitude, latitude) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        c.execute(insert_query, (self.id, self.name_place, self.num_street, self.street, self.place_says, self.city, self.city_code, self.longitude, self.latitude))

    def select_list_city(self, db):
        c = db.con.cursor()
        query =  "SELECT city FROM place "
        c.execute(query)
        tab=[]
        for row in c.fetchall():
            tab.append(row[0])
        tab = set(tab)
        locale.setlocale(locale.LC_ALL, "fr_FR.UTF-8")
        x = [a for a in sorted(tab, key=locale.strxfrm)]
        return x

#"Nom usuel de l'installation","Numéro de l'installation","Nom de la commune","Code INSEE","Code postal","Nom du lieu dit","Numero de la voie","Nom de la voie","location","Longitude","Latitude","Aucun aménagement d'accessibilité","Accessibilité handicapés à mobilité réduite","Accessibilité handicapés sensoriels","Emprise foncière en m2","Gardiennée avec ou sans logement de gardien","Multi commune","Nombre total de place de parking","Nombre total de place de parking handicapés","Installation particulière","Desserte métro","Desserte bus","Desserte Tram","Desserte train","Desserte bateau","Desserte autre","Nombre total d'équipements sportifs","Nombre total de fiches équipements","Date de mise à jour de la fiche installation"
