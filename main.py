from db import Db
from FileCSV import FileCSV
from place import Place
from equipement import Equipement
from activity import Activity
from equipementactivity import EquipementActivity

DB = Db()
DB.create_table()
DB.commit()

#Insert in db of place
file = FileCSV('fichiersCSV/23440003400026_J335_installations_table.csv')
csv = file.print_line_except_first()
for row in csv:
    p = Place()
    p.create_object(row)
    DB.insert_in_place(p)
DB.commit()

#Insert in db equipement
file = FileCSV('fichiersCSV/equipements.csv')
csv = file.print_line_except_first()
for row in csv:
    e = Equipement()
    e.create_object(row)
    DB.insert_in_equipement(e)
DB.commit()

#Insert in db of activity
file = FileCSV('fichiersCSV/J334_equipements_activites.csv')
csv = file.print_line_except_first()
for row in csv:
    a = Activity()
    a.create_object(row)
    if not(not(row[5])):
        if a.exist_in_DB(DB)==False:
            a.insert(DB)
DB.commit()

#Insert in db of equipement-activity
csv = file.print_line_except_first()
for row in csv:
    ea = EquipmentActivity()
    ea.create_object(row)
    if not(not(row[5])):
        if ea.exist_in_DB(DB)==False:
            ea.insert_in_DB(DB)
DB.commit()
DB.deconnect()
