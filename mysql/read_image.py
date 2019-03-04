import MySQLdb as mdb 

def writeImage(data,name):
    fout = open(name, 'wb')
    with fout:
        fout.write(data)


con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
with con:
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT photo,name FROM Image WHERE id=1")
    data = cur.fetchone()
    writeImage(data['photo'],data['name'])  


create
insert 
update
delete

images