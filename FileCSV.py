import csv

class FileCSV:
	def __init__(self,name):
		self.name = name

	#return tab of CSV file
	def print_file(self):
		tab =[]
		with open(self.name) as file:
			reader = csv.reader(file)
			for row in reader:
				tab.append(row)
		return tab

	#print a specific line
	def print_line(self,line):
		tab = self.print_file()
		return tab[column]

	#print line to line
	def print_multiple_line(self,l1,l2):
		tab = self.print_file()
		return tab[l1:l2+1]

	def print_line_except_first(self):
		tab = self.print_file()
		return tab[1:len(tab)]

"""
f=FileCSV('fichiersCSV/23440003400026_J335_installations_table.csv')
tab = f.print_file()
print(tab[0][1])
print('\n')
tab2 = f.print_column(0)
print(tab2)
print('\n')
tab3 = f.print_multiple_column(1,2)
print(tab3)
#print(tab)
#tab2 = ['coucou',tab]
"""
