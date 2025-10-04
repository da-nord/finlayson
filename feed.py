import feedparser
import webbrowser

feed = feedparser.parse("https://finance.yahoo.com/rss/")

feed_title = feed['feed']['title']
feed_entries = feed.entries

for entry in feed.entries:

    article_title = entry.title
    article_link = entry.link
    article_published_at = entry.published # Unicode string
    article_published_at_parsed = entry.published_parsed # Time object
    article_author = entry.author
    content = entry.summary
    article_tags = entry.tags


    print ("{}[{}]".format(article_title, article_link))
    print ("Published at {}".format(article_published_at))
    print ("Published by {}".format(article_author))
    print("Content {}".format(content))
    print("catagory{}".format(article_tags))