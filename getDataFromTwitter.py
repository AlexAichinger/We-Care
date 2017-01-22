
import MySQLdb
from nlp import NLPMain
from vision import VisionMain

class GetDataFromTwitter:
	uid = 30;
	mainNLPObject =  NLPMain()
	mainVisionObject = VisionMain()


	conn = MySQLdb.connect("104.198.178.129", "mutherrussia", "trump", "db_wecare")

	c = conn.cursor()

	status = 0

	try:
		c.execute("Select status_p,pic FROM getInfoTwitter where uuid = 30")
		results = c.fetchall()
		for row in results:
			status = row[0]
			NLPscore = mainNLPObject.sentiment_text(status)
			print (NLPscore + " is the NLPScore")
			pic = row[1]
			visionScore = mainVisionObject.faces_uri(pic)
			print(visionScore + "is the Vision Score")
			

	except:
		print "Error: unable to fetch data"

	conn.close()	

	
	

	

	