
import mySQLdb
import time
import json
import urllib2
import urllib

conn = MySQLdb.connect("146.148.37.239", "root", "314159", "socialInfo")

class listener():

    url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=196701503.1c6771e.08d31360dd0b443c886e961e22f865f0"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    for i in range(20):
        d = data["data"][i]["images"]["standard_resolution"]["url"]
        c = data["data"][i]["caption"]["text"]
        c.execute("INSERT INTO getInfoInsta (pic,status, timestamp,uid,username) VALUES (%s,%s,%s,%s,%s)",(d, c, "00:40", "Kevin", "Kevingotlayed"))
        conn.commit()
        print d
        print c
