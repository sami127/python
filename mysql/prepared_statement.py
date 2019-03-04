import MySQLdb as mdb
con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
with con:    
    cur = con.cursor()
    cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s",("Kavitha", "4"))        
    print ("Number of rows updated:",  cur.rowcount)


# update Writers set name="Samiulla" where id=1

# def update_db(name,id):
#     cur.execute("update Writers set name=%s where id=%s",(name,id))