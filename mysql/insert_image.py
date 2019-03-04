import MySQLdb as mdb
import time
def read_image():
	with open("download.jpeg",'rb') as f:
		img = f.read()
		return img
con = mdb.connect('localhost', 'testuser', 'test623', 'testdb')
#Create database table here for image storing
# with con:
# 	cur = con.cursor()
# 	cur.execute("CREATE TABLE IF NOT EXISTS Image (id INT PRIMARY KEY AUTO_INCREMENT, \
# 	photo BLOB NOT NULL, name VARCHAR(500))")
with con:
	cur = con.cursor()
	data = read_image()
	millis = int(round(time.time() * 1000))
	cur.execute("INSERT INTO Image (photo,name) VALUES(%s, %s)", \
		(data, 'first_image'+str(millis)+'.jpg'))

