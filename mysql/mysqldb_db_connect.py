import MySQLdb as mdb
import sys

try:
    con = mdb.connect('localhost', 'testuser', 'test6293', 'testdb')

    cur = con.cursor()
    cur.execute("SELECT VERSION()")

    ver = cur.fetchone()
    
    print ("Database version : %s " % ver)
    
except mdb.Error as e:
    print ("Error %d: %s" % (e.args[0],e.args[1]))
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()