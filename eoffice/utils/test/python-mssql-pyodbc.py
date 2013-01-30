import pyodbc
cnxn = pyodbc.connect("DRIVER={SQL Server};SERVER=ganbolor;DATABASE=testdb;UID=sa;PWD=123;Trusted_Connection=1")
cursor = cnxn.cursor()
cursor.execute("select user_id, user_name from users")
rows = cursor.fetchall()
for row in rows:
    print row.user_id, row.user_name