
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

    def exist_in_DB(self, DB):
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
        c = DB.con.cursor()
        insert_query = "INSERT INTO activity(id, name_activity, level_activity) VALUES (?, ?, ?)"
        c.execute(insert_query, (self.id, self.name_activity, self.level_activity))

    def select_list(self, DB):
        c = DB.con.cursor()
        query =  "SELECT name_activity FROM activity "
        c.execute(query)
        tab=[]
        for row in c.fetchall():
            tab.append(row[0])
        tab.sort()
        return tab

    def select_list_in_city(self, DB, city):
        c = DB.con.cursor()
        lcity = "'"+city+"'"
        query =  "SELECT * FROM activity WHERE id in (SELECT id_activity FROM equipementactivity WHERE id_equipement in (SELECT id FROM equipement WHERE num_place in (SELECT id FROM place where city={0})))".format(lcity)
        c.execute(query)
        tab=[]
        for row in c.fetchall():
            a = Activity()
            a.id = row[0]
            a.name_activity = row[1]
            a.level_activity = row[2]
            tab.append(a)
        tab = set(tab)
        return tab

#ComInsee,"ComLib",EquipementId,EquNbEquIdentique,ActCode,"ActLib","EquActivitePraticable","EquActivitePratique","EquActiviteSalleSpe","ActNivLib"
