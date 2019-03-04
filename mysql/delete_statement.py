import MySQLdb as mdb
con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
with con:    
    cur = con.cursor()
    cur.execute("delete from Writers where Id=2")        
    print ("Number of rows updated:",  cur.rowcount)
