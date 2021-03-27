import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ORENBER-PC\MSSQLSERVER2008;'
                      'Database=RealEstate;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM purchase')

for row in cursor:
    print(row)