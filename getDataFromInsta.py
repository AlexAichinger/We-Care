import MySQLdb

uid = 30;


conn = MySQLdb.connect("104.198.178.129", "mutherrussia", "trump", "db_wecare")

c = conn.cursor()

try:
	c.execute("Select status_p FROM getInfoInsta where uuid = 30")
	results = c.fetchall()
	for row in results:
		status = row[0]
		print status

except:
	print "Error: unable to fetch data"

conn.close()	


