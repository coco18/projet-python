
class Activity:
    """docstring for """
    def __init__(self):
        self.id = None
        self.name_activity = None
        self.level_activity = None

    """docstring for equipement"""
    def create_object(self, tab):
        self.id = tab[4]
        self.name_activity = tab[5]
        self.level_activity = tab[9]
    def listActivity(self, id):
        """"list of activity"""


#ComInsee,"ComLib",EquipementId,EquNbEquIdentique,ActCode,"ActLib","EquActivitePraticable","EquActivitePratique","EquActiviteSalleSpe","ActNivLib"
