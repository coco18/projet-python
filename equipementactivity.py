
class EquipementActivity():
    """docstring for EquipementActivity"""
    def __init__(self):
        self.id_equipement = None
        self.id_activity = None

    def create_object(self, tab):
        self.id_equipement = tab[2]
        self.id_activity = tab[4]




    #ComInsee,"ComLib",EquipementId,EquNbEquIdentique,ActCode,"ActLib","EquActivitePraticable","EquActivitePratique","EquActiviteSalleSpe","ActNivLib"
