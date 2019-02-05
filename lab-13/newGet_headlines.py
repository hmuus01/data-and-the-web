from flask import Flask, render_template
from flask import request
import feedparser

app = Flask(__name__)

RSS_FEEDS = { 'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
              'aljazeera' : 'https://www.aljazeera.com/xml/rss/all.xml',
	      'sky': 'http://feeds.skynews.com/feeds/rss/politics.xml',
	      'cbs': 'http://www.CBSNews.com.xml',
              'ap':\
              'http://hosted2.ap.org/atom/APDEFAULT/cae69a7523db45408eeb2b3a98c0c9c5'}


@app.route("/")
def headlines():
    publication =''
    if request.args.get('publication'):
        publication = request.args.get('publication')
    if not publication or publication.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = publication.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    articles = feed['entries']
    return render_template('newGet_headlines.html',articles=articles)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)

