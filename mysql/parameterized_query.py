import MySQLdb as mdb
try:
    con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
    cursor = con.cursor()
    #Update single record now
    sql_parameterized_query = """Update Writers set name = %s where id = %s"""
    name = 'Jack'
    id = 1
    input = (name, id)
    cursor.execute(sql_parameterized_query , input)
    con.commit()
    print("Record Updated successfully using prepared stament")
except mdb.Error as e:
    print ("Error %d: %s" % (e.args[0],e.args[1]))
    sys.exit(1)
finally:
    #closing database connection.
    if con:    
        con.close()