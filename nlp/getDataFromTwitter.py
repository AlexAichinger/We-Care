
import MySQLdb
from nlp import NLPMain

class GetDataFromTwitter:
	uid = 30;


	conn = MySQLdb.connect("104.198.178.129", "mutherrussia", "trump", "db_wecare")

	c = conn.cursor()

	status = 0

	try:
		c.execute("Select status_p FROM getInfoTwitter where uuid = 30")
		results = c.fetchall()
		for row in results:
			status = row[0]
			print status

	except:
		print "Error: unable to fetch data"

	conn.close()	

	mainObject =  NLPMain()

	score = mainObject.sentiment_text(status)
	print (score)