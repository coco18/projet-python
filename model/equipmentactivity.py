
class EquipmentActivity():
    """docstring for EquipementActivity"""
    def __init__(self):
        self.id_equipment = None
        self.id_activity = None

    def create_object(self, tab):
        self.id_equipment = tab[2]
        self.id_activity = tab[4]

    def insert_in_DB(self, DB):
        c = DB.con.cursor()
        insert_query = "INSERT INTO equipmentactivity(id_equipment, id_activity) VALUES (?, ?)"
        c.execute(insert_query, (self.id_equipment, self.id_activity))

    def exist_in_DB(self, DB):
        c = DB.con.cursor()
        insert_query = "SELECT id_activity FROM equipmentactivity WHERE id_equipment=(?)"
        c.execute(insert_query, (self.id_equipment,))
        tmp=None
        exist=False
        for row in c:
            tmp = row[0]
            if tmp==int(self.id_activity):
                exist=True
        if exist:
            return True
        else:
            return False


    #ComInsee,"ComLib",EquipementId,EquNbEquIdentique,ActCode,"ActLib","EquActivitePraticable","EquActivitePratique","EquActiviteSalleSpe","ActNivLib"
