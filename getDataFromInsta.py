import MySQLdb
from nlp import NLPMain
from vision import VisionMain

class GetDataFromInsta:
	uid = 30;
	my_list = []
	counter = 1

	mainNLPObject =  NLPMain()
	mainVisionObject = VisionMain()
	conn = MySQLdb.connect("104.198.178.129", "mutherrussia", "trump", "db_wecare")
	c = conn.cursor()
	tempStr = ""

	c.execute("Select status_p FROM getInfoInsta where uuid = 30")
	results = c.fetchall()
	for row in results:
		status = row[0]
	#	print status
		
	t = row[0]
	print t
	NLPscore = mainNLPObject.sentiment_text(status)
	print (NLPscore)



	conns = MySQLdb.connect("104.198.178.129", "mutherrussia", "trump", "db_wecare")

	cs = conns.cursor()
	tempStr = ""

	cs.execute("Select pic FROM getInfoInsta where uuid = 30")
	result = cs.fetchall()
	for row in result:
		status = row[0]
		visionScore = mainVisionObject.faces_uri(pic)
		print(visionScore)
	#	print status
		
	s = row[0]

	s = s.split(' ');

	for i in range(len(s)):
		print s[i]

	conn.close()