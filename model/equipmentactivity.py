
class EquipmentActivity():
    """docstring for EquipementActivity"""
    def __init__(self):
        self.id_equipment = None
        self.id_activity = None

    def create_object(self, tab):
        """Creation of the EquipmentActivity
    	:param tab: Array with the attribute of a equipment
    	:type tab: array 
    	"""
        self.id_equipment = tab[2]
        self.id_activity = tab[4]

    def insert_in_DB(self, DB):
         """insert the place in a table
    	:param db: the database who contains the table
    	:type db: base
    	"""
        c = DB.con.cursor()
        insert_query = "INSERT INTO equipmentactivity(id_equipment, id_activity) VALUES (?, ?)"
        c.execute(insert_query, (self.id_equipment, self.id_activity))

    def exist_in_DB(self, DB):
    	"""Verify if the equipmentActivity exist in our table
    	:param db: the base who contains the table
    	:type db: base
    	:rtype: boolean
    	"""    
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
