import csv

class FileCSV:
	def __init__(self,name):
		self.name = name

	#print a CSV file
	def printfile(self):
		with open(self.name, newline='\n') as file:
			reader = csv.reader(file)
			for row in reader:
				print(row)

	#print a specific column
	def printcolumn(self,column):
		with open(self.name, newline='\n') as file:
			reader = csv.reader(file)
			for row in reader:
				print(row[column])

	#print more than one column, col1 and col2 are numbers
	def printmultiplecolumn(self,col1,col2):
		with open(self.name, newline='\n') as file:
			reader = csv.reader(file)
			for row in reader:
				for i in range(col1,col2):
					print(row[i]+',')


f=FileCSV('23440003400026_J335_installations_table.csv')
f.printfile()
tab = ['test']
tab2 = ['coucou',tab]
