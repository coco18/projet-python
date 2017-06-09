from operator import itemgetter, attrgetter, methodcaller

class Activity:
    """docstring for activity"""
    def __init__(self):
        self.id = None
        self.name_activity = None
        self.level_activity = None

    def create_object(self, tab):
        """Creation of the activity
    	:param tab: Array with the attribute of an activity
    	:type tab: array
    	"""
        self.id = tab[4]
        self.name_activity = tab[5]
        self.level_activity = tab[9]

    def exist_in_DB(self, DB):
        """Verify if the activity exist in our table
        :param db: the base who contains the table
        :type db: base
    	:rtype: boolean
    	"""
        c = DB.con.cursor()
        insert_query = "SELECT id FROM activity WHERE id=(?)"
        c.execute(insert_query, (self.id,))
        tmp=None
        for row in c:
            tmp = row[0]
        if tmp==int(self.id):
            return True
        else:
            return False

    def insert_in_DB(self, DB):
        """insert the activity in a table
        :param db: the database who contains the table
        :type db: base
        """
        c = DB.con.cursor()
        insert_query = "INSERT INTO activity(id, name_activity, level_activity) VALUES (?, ?, ?)"
        c.execute(insert_query, (self.id, self.name_activity, self.level_activity))

    def select(self, db, idactivity):
        """Assign the value of the activity passes in parameters to the actual activity
        :param db: the base who contains the table
        :type db: base
        :param idequipment: the identifiant of the activity
        :type idequipment: int
        """
        c = db.con.cursor()
        query = "SELECT * FROM activity WHERE id={0} ".format(idactivity)
        c.execute(query)
        row = c.fetchone()
        self.id = row[0]
        self.name_activity = row[1]
        self.level_activity = row[2]

    def select_list(self, DB):
        """Give all the activities we know
        :param db: the base who contains the table
        :type db: base
        :returns: tab
        :rtype: Activity[]
        """
        c = DB.con.cursor()
        query =  "SELECT * FROM activity "
        c.execute(query)
        tab=[]
        for row in c.fetchall():
            a = Activity()
            a.id = row[0]
            a.name_activity = row[1]
            a.level_activity = row[2]
            tab.append(a)

        return sorted(tab, key=attrgetter('name_activity'))

    def select_list_in_city(self, DB, city):
        """Give all the activities in a city
    	:param db: the base who contains the table
    	:type db: base
    	:param city: the name of the city
    	:type city: name
    	:returns: tab
    	:rtype: Activity[]
    	"""
        c = DB.con.cursor()
        lcity = "'"+city+"'"
        query =  "SELECT * FROM activity WHERE id in (SELECT id_activity FROM equipmentactivity WHERE id_equipment in (SELECT id FROM equipment WHERE num_place in (SELECT id FROM place where city={0})))".format(lcity)
        c.execute(query)
        tab=[]
        for row in c.fetchall():
            a = Activity()
            a.id = row[0]
            a.name_activity = row[1]
            a.level_activity = row[2]
            tab.append(a)
        return sorted(tab, key=attrgetter('name_activity'))

#ComInsee,"ComLib",EquipementId,EquNbEquIdentique,ActCode,"ActLib","EquActivitePraticable","EquActivitePratique","EquActiviteSalleSpe","ActNivLib"
