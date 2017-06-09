from db.db import Db
from db.FileCSV import FileCSV
from model.place import Place
from model.equipment import Equipment
from model.activity import Activity
from model.equipmentactivity import EquipmentActivity

DB = Db()
DB.create_table()
DB.commit()

#Insert the table place in database
file = FileCSV('fichiersCSV/23440003400026_J335_installations_table.csv')
csv = file.print_line_except_first()
for row in csv:
    p = Place()
    p.create_object(row)
    p.insert(DB)
DB.commit()

#Insert the table equipment in database
file = FileCSV('fichiersCSV/equipements.csv')
csv = file.print_line_except_first()
for row in csv:
    e = Equipment()
    e.create_object(row)
    e.insert(DB)
DB.commit()

#Insert the table activity in database
file = FileCSV('fichiersCSV/J334_equipements_activites.csv')
csv = file.print_line_except_first()
for row in csv:
    a = Activity()
    a.create_object(row)
    if not(not(row[5])):
        if a.exist_in_DB(DB)==False:
            a.insert_in_DB(DB)
DB.commit()

#Insert the table equipmentactivity in database
csv = file.print_line_except_first()
for row in csv:
    ea = EquipmentActivity()
    ea.create_object(row)
    if not(not(row[5])):
        if ea.exist_in_DB(DB)==False:
            ea.insert_in_DB(DB)
DB.commit()
DB.deconnect()
