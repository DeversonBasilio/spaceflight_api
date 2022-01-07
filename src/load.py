
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column,ForeignKey
from sqlalchemy.types import Integer, String, Boolean
from sqlalchemy import event
import requests
import json

engine = create_engine("mysql+pymysql://ifa5jh31yxnmydus:klitwc7ub1m0hvh6@l6glqt8gsx37y4hs.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/r1spg75hiiwyd8uq")

meta = MetaData()
conn = engine.connect()

r = requests.get('https://api.spaceflightnewsapi.net/v3/articles')

packages_json = r.json()

with open('data.json', 'w') as outfile:
    json.dump(packages_json, outfile)


articles1 = []
events1 = []
launches1 = []

# read file

with open("data.json", "r") as read_it:
     data = json.load(read_it)


articles = Table(
    'articles',meta,
    Column('id',Integer,primary_key=True),
    Column('featured',Boolean,default=False),
    Column('title',String(255)),
    Column('url',String(255)),
    Column('imageUrl',String(255)),
    Column('newsSite',String(255)),
    Column('summary',String(255)),
    Column('publishedAt',String(255))
)

launches = Table (
    'launches',meta,
    Column('id',String(255), primary_key=True),
    Column('provider',String(255)),
    Column('article_id',Integer, ForeignKey('articles.id'))
)


events = Table (
    'events',meta,
    Column('id',Integer,primary_key=True),
    Column('provider',String(255)),
    Column('article_id',Integer, ForeignKey('articles.id'),primary_key=True)
)

for article in data:
    
    art = {
        "id":article["id"],
        "featured":article["featured"],
        "title":article["title"],
        "url":article["url"],
        "imageUrl":article["imageUrl"],
        "newsSite":article["newsSite"],
        "summary":article["summary"],
        "publishedAt": article["publishedAt"],    
    }

    articles1.append(art)

    for event in article['events']:
        ev = {
            "id":event["id"],
            "provider":event["provider"],
            "article_id": article['id']        
        }

        events1.append(ev)
    
    for launche in article['launches']:
        lnc = {
            "id":launche["id"],
            "provider":launche["provider"],
            "article_id": article['id']        
        }

        launches1.append(lnc)

conn.execute(articles.insert(articles1,prefixes=['IGNORE']))
conn.execute(launches.insert(launches1,prefixes=['IGNORE']))
conn.execute(events.insert(events1,prefixes=['IGNORE']))
