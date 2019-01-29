from flask import Flask, render_template
import feedparser
from random import randint
app = Flask(__name__)
BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
@app.route("/")
def headline():
    feed = feedparser.parse(BBC_FEED)
    articles = feed['entries']
    return render_template("feed.html",newsFeed=articles)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
