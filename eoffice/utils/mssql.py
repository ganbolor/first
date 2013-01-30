import pymssql
conn = pymssql.connect(host='192.168.10.1', user='user1', password='higanaa', database='Test')
cur = conn.cursor()

#cur.execute('CREATE TABLE persons(id INT, name VARCHAR(100))')
#cur.executemany("INSERT INTO persons VALUES(%d, %s)", \
#    [ (1, 'John Doe'), (2, 'Jane Doe') ])
#conn.commit()  # you must call commit() to persist your data if you don't set autocommit to True



#cur.execute("SELECT * FROM ( SELECT id, ROW_NUMBER() OVER (ORDER BY id) as row  FROM View_ssCustomers   ) a WHERE row > 0 and row <= 10")
cur.execute("SELECT TOP 10 * FROM View_ssCustomers ORDER BY ActionDate DESC  ")



row = cur.fetchone()
ids=0

while row:
    ids=ids+1
    
    print "ID=%d, Name=%s" % (ids, row[0], row[1])
    
    
    row = cur.fetchone()

# if you call execute() with one argument, you can use % sign as usual
# (it loses its special meaning).
cur.execute("SELECT * FROM persons WHERE name LIKE 'J%'")

conn.close()
