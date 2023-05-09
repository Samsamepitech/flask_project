from flask import Flask, redirect
from flask import url_for
import feedparser
from json import load
from flask import render_template


#json file reading
with open("./static/link_rss.json","r", encoding ="utf-8") as fd:
  link_rss=load(fd)


#function that returns the sublinks :
def flux_rss(link):
  feed = feedparser.parse(link)
  flux_rss=feed.entries
  array=[]
  for i in range(len(flux_rss)):
    array.append(flux_rss[i].link)
  return (array)



#function that returns the sublinks title :
def lien(title):
  feed = feedparser.parse(title)
  flux_rss=feed.entries
  array2=[]
  for i in range(len(flux_rss)):
    array2.append(flux_rss[i].title)
  return (array2)



#Flask app declaration
app = Flask(__name__)


#home route 
@app.route("/")

def feed_rss():
  return render_template('home.html', link_rss=link_rss, flux=flux)


#Subfeeds links
@app.route('/<RSS>')
        
def flux(RSS):
  FEED=flux_rss(link_rss[RSS])
  TITLE=lien(link_rss[RSS])
  return render_template('links.html',FEED=FEED, TITLE=TITLE,RSS=RSS )

#blog route 
@app.route("/blog")

def blog():
  return render_template('blog.html')

#blog route 
@app.route("/contact")

def contact():
  return render_template('contact.html')

