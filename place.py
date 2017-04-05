

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


#"Nom usuel de l'installation","Numéro de l'installation","Nom de la commune","Code INSEE","Code postal","Nom du lieu dit","Numero de la voie","Nom de la voie","location","Longitude","Latitude","Aucun aménagement d'accessibilité","Accessibilité handicapés à mobilité réduite","Accessibilité handicapés sensoriels","Emprise foncière en m2","Gardiennée avec ou sans logement de gardien","Multi commune","Nombre total de place de parking","Nombre total de place de parking handicapés","Installation particulière","Desserte métro","Desserte bus","Desserte Tram","Desserte train","Desserte bateau","Desserte autre","Nombre total d'équipements sportifs","Nombre total de fiches équipements","Date de mise à jour de la fiche installation"
