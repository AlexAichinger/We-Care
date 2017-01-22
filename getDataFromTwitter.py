
import MySQLdb
from nlp import NLPMain
from vision import VisionMain

class GetDataFromTwitter:
	uid = 30;


	conn = MySQLdb.connect("104.198.178.129", "mutherrussia", "trump", "db_wecare")

	c = conn.cursor()

	status = 0

	try:
		c.execute("Select status_p,pic FROM getInfoTwitter where uuid = 30")
		results = c.fetchall()
		for row in results:
			status = row[0]
			pic = row[1]
			print status

	except:
		print "Error: unable to fetch data"

	conn.close()	

	mainNLPObject =  NLPMain()

	NLPscore = mainNLPObject.sentiment_text(status)
	print (NLPscore)

	mainVisionObject = VisionMain()

	visionScore = mainVisionObject.faces_uri(pic)
	print(visionScore)