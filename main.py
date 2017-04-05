from db import Db
from FileCSV import FileCSV
from place import Place

DB = Db()
DB.create_table()
file = FileCSV('fichiersCSV/23440003400026_J335_installations_table.csv')
csv = file.print_line_except_first()
for row in csv:
    p = Place()
    p.create_object(row)
    DB.insert_in_place(p)
