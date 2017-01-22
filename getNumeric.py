import MySQLdb
import argparse
import io
import os
import urllib
import base64
import argparse

from google.cloud import language


from google.cloud import vision

uid = 30;
counter = 1
VERY_UNLIKELY_VARIABLE = 1
VERY_LIKELY_VARIABLE = 1
superAvg = 1

def detect_faces_from_uri(uri):
    """Detects faces in an image."""
    vision_client = vision.Client()

    url = uri
    opener = urllib.urlopen(url)

    content = opener.read()

    image = vision_client.image(content=content)

    faces = image.detect_faces()


    '''
    for face in faces:
        print('Faces:')
        print('anger: {}'.format(face.emotions.anger))
        print('joy: {}'.format(face.emotions.joy))
        print('surprise: {}'.format(face.emotions.surprise))
    '''
    #print format(faces.emotions.anger)
    sum =0
    counter = 1
    for face in faces:
        #print('anger: {}'.format(face.emotions.anger))
        counter+=1

        str1 = (format(face.emotions.anger))
        
        if str1 == "Likelihood.VERY_UNLIKELY":
            sum += 0.7*(VERY_UNLIKELY_VARIABLE)
        else:
            sum += -0.7*(VERY_LIKELY_VARIABLE)

        str2 = (format(face.emotions.sorrow))

        if str2 == "Likelihood.VERY_UNLIKELY":
            sum += 0.85*(VERY_UNLIKELY_VARIABLE)
        else:
            sum += -0.85*(VERY_LIKELY_VARIABLE)

        str3 = (format(face.emotions.joy))

        if str3 == "Likelihood.VERY_UNLIKELY":
            sum += -0.2*(VERY_UNLIKELY_VARIABLE)
        else:
            sum += (VERY_LIKELY_VARIABLE)

        print("#####################")

        #print('joy: {}'.format(face.emotions.joy))
        #print('surprise: {}'.format(face.emotions.surprise))

    avg = sum/(3*counter)
    
    print(str(avg) + " is the average")

    return avg

def createConnection():
    conn = MySQLdb.connect("104.198.178.129", "mutherrussia", "trump", "db_wecare")

    c = conn.cursor()
    tempStr = ""

    c.execute("Select status_p FROM getInfoInsta where uuid = 30")
    results = c.fetchall()
    for row in results:
        status = row[0]
    #   print status
        
    t = row[0]
    print t



    conns = MySQLdb.connect("104.198.178.129", "mutherrussia", "trump", "db_wecare")

    cs = conns.cursor()
    tempStr = ""

    cs.execute("Select pic FROM getInfoInsta where uuid = 30")
    result = cs.fetchall()
    for row in result:
        status = row[0]
    #   print status
        
    s = row[0]

    s = s.split(' ');
    # to get rid of blank result at end

    superAvg = 0

    for i in range(len(s)-1):
        #print s[i]
        #print detect_faces_from_uri(s[i])
        #print "__________________________"
        superAvg += detect_faces_from_uri(s[i])


    connt = MySQLdb.connect("104.198.178.129", "mutherrussia", "trump", "db_wecare")

    ct = connt.cursor()

    statusT = ""

    try:
        ct.execute("Select status_p,pic FROM getInfoTwitter where uuid = 1")
        resultT = ct.fetchall()
        for row in resultT:
            statusT = row[0]
            #NLPscore = mainNLPObject.sentiment_text(status)
            #print (NLPscore + " is the NLPScore")
        print statusT
            #visionScore = mainVisionObject.faces_uri(pic)
            #print(visionScore + "is the Vision Score")
            

    except:
        print "Error: unable to fetch data"

    connt.close()   


    conn.close()
    conns.close()
    print("EN METHOD " + os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
    return GetFinalAns(t,superAvg,statusT,s)





def sentiment_text(text):
    """Detects sentiment in the text."""
    language_client = language.Client()

    # Instantiates a plain text document.
    document = language_client.document_from_text(text)

    # Detects sentiment in the document. You can also analyze HTML with:
    #   document.doc_type == language.Document.HTML
    sentiment = document.analyze_sentiment()

    print('Score: {}'.format(sentiment.score))
    nlpScore = format(sentiment.score)
    print('Magnitude: {}'.format(sentiment.magnitude))

    return nlpScore





def GetFinalAns(t,superAvg,statusT,s):



    nlpScore = sentiment_text(t)
    superAvg = superAvg/(len(s)-1)

    print(superAvg)



    print "twitter nlp"
    t = sentiment_text(statusT)
    print(t + " is the NLP score for twitter")

    print "Final data :"
    finalAns = (float(t) + float(nlpScore) + superAvg)/3
    print (finalAns)


    return finalAns




