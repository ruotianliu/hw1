import tweepy
from tweepy import OAuthHandler
import json
import wget
import os
import PIL
from PIL import Image
import io
from google.cloud import vision
from google.cloud.vision import types
import pymysql
import sys

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
 
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
# User() is the data model for a user profil
tweepy.models.User.first_parse = tweepy.models.User.parse
tweepy.models.User.parse = parse
# You need to do it for all the models you need
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

twitter_id = sys.argv[1]

tweets = api.user_timeline(screen_name=twitter_id,count=200, include_rts=False,exclude_replies=True)

last_id = tweets[-1].id
 
while (True):
    more_tweets = api.user_timeline(screen_name=twitter_id,count=200,include_rts=False,exclude_replies=True,max_id=last_id-1)
# There are no more tweets
    if (len(more_tweets) == 0):
      break
    else:
      last_id = more_tweets[-1].id-1
      tweets = tweets + more_tweets

media_files = set()
for status in tweets:
    media = status.entities.get('media', [])
    if(len(media) > 0):
        media_files.add(media[0]['media_url'])

for media_file in media_files:
    wget.download(media_file)
    
path = os.getcwd()

filelist = os.listdir(path)
total_num = 0
i = 0
for item in filelist:
    if item.endswith('.jpg'):
         src = os.path.join(os.path.abspath(path), item)
         dst = os.path.join(os.path.abspath(path), 'img' + format(str(i), '0>3s') + '.jpg')
         os.rename(src, dst)
         i = i + 1
         total_num = total_num + 1
i=0
for item in filelist:
    if item.endswith('.jpg'):
         img=Image.open(item)
         img_resized=img.resize((768,576),PIL.Image.ANTIALIAS)
         img_resized.save('img'+format(str(i),'0>3s')+'.jpg')
         i=i+1


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""
def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    label_list = []
    
    image = vision.types.Image(content=content)
   
    response = client.label_detection(image=image)
    labels = response.label_annotations
    
    for label in labels:
        label_list.append(label.description)
    return label_list

for i in range(10):
    PATH=os.getcwd()
    labels = detect_labels(PATH+'/'+'img00'+str(i)+'.jpg')
    
    #connect to database
    db = pymysql.connect("localhost", "root", "lrtbest2018", "test")
    myCursor = db.cursor()
        
    #insert colunms into table tweetsInfomation
    try:
        sqlFormula = "INSERT INTO tweetsInfomation (name, image_id, image_num, label) VALUES (\'%s\', \'%s\', \'%s\', \'%s\')" % (twitterID, i, total_num, labels)
  
        myCursor.execute(sqlFormula)
        db.commit()
    except:
        print("can not insert columns")
        db.rollback()
        db.close()
        
for i in range(10,12):
    PATH=os.getcwd()

    labels = detect_labels(PATH+'/'+'img0'+str(i)+'.jpg')


    #connect to database
    db = pymysql.connect("localhost", "root", "lrtbest2018", "test")
    myCursor = db.cursor()
        
    #insert colunms into table tweetsInfomation
    try:
        sqlFormula = "INSERT INTO tweetsInfomation (name, image_id, image_num, label) VALUES (\'%s\', \'%s\', \'%s\', \'%s\')" % (twitterID, i, total_num, labels)
  
        myCursor.execute(sqlFormula)
        db.commit()
    except:
        print("can not insert columns")
        db.rollback()
        db.close()