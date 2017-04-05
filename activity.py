
class activity:
    self.id
    self.name_activity
    self.level_activity

    """docstring for equipement"""
    def create_object(self, tab):
        self.id = tab[4]
        self.name_activity = tab[5]
        self.level_activity = tab[9]
    def listActivity(self, id):
        """"list of activity"""


#ComInsee,"ComLib",EquipementId,EquNbEquIdentique,ActCode,"ActLib","EquActivitePraticable","EquActivitePratique","EquActiviteSalleSpe","ActNivLib"
