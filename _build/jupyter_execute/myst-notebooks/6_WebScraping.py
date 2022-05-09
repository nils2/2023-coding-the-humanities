#!/usr/bin/env python
# coding: utf-8

# # Web Scraping and APIs
# 
# In this notebook, we learn how to scrape data from the Web and get an idea of what Applicaiton Programming Interfaces are (APIs).

# ## Web Scraping
# 
# **Web Scraping** is a technique for the extraction of information from websites by transforming unstructured data (HTML pages) into structured data (databases or spreadsheets). 
# 
# Even if scraping can be manually performed by a user, it is usually implemented using a **web crawler** (i.e., it is usually implemented as an automatic process). For larger scale scraping see, e.g., [Scrapy](https://scrapy.org).

# The process is an alternative to using already available **API**s (Application Programming Interface), such as those provided by all the major platforms, like *Facebook*, *Google* and *Twitter*. **More below.**

# ### Basics of HTML
# 
# The **HyperText Markup Language (HTML)** is the standard **descriptive markup** language for web pages.
# 
# 
# - **Markup** language: a human-readable, explicit system for annotating the content of a document. Markdown is another markup language.
# 
# 
# - **Descriptive** markup languages (e.g. HTML, XML) are used to annotate the structure or the contents of a document, as opposed to **procedural** markup languages (e.g. TEX, Postscript), whose main goal is to describe how a document should be processed.

# HTML provides a means to annotate the <strong>structural</strong> elements of documents like (different kinds of) headings, paragraphs, lists, links, images, quotes, tables and so forth. Similarly, even if with fewer options, does Markdown (which we are <em>using</em> *here*, check the code!).
# 
# HTML tags **do not mark the logical structure** of a document, but only its format (e.g. *this is a table*, *this is a h3-type heading*...). It is up to the browser to then use HTML (plus other information, such as *Cascading Style Sheets*), to render a webpage appropriately.

# HTML markup relies on a **fixed inventory of tags**, written by using angle brackets. Some tags, e.g. `<p>...</p>`, surround the marked text, and may include subelements. Other tags, e.g. `<br>` or `<img>` introduce content directly.
# 
# The following is an example of a web page:
# 
# ```html
# <!DOCTYPE html>
# <html>
#   <head>
#     <title>The Adventures of Pinocchio</title>
#   </head>
#   <body>
#     <h2>Carlo Collodi</h2>
#     <h1>The Adventures of Pinocchio</h1>
#     <hr>
#     <h4>CHAPTER 1</h4>
#     <br>
#     <p><i>How it happened that Mastro Cherry, carpenter, found a piece of wood that wept and laughed like a child</i></p>
#     <br>
#     <p>Centuries ago there lived--</p>
#     <p>"A king!" my little readers will say immediately.</p>
#   </body>
# </html>
# ```

# ### Scraping Web Pages

# ```{note}
# The following notes are roughly based on the **Chapters 1-3** of: Mitchell, R. (2015). [Web Scraping with Python](http://shop.oreilly.com/product/0636920034391.do), O'Reilly
# ```

# #### Modules and Packages Required for Web Scraping
# 
# **BeautifulSoup**: this library defines [classes and functions](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to pull data (e.g. table, lists, paragraphs) out of HTML and XML files. It provides idiomatic ways of navigating, searching, and modifying the parse tree.
# 
# 
# **lxml**: to function, BeautifulSoup relies on external HTML-XML parsers. Many options are available, among which the html5lib's and the Python's built-in parsers. We'll rely on the [lxml](http://lxml.de/)'s parser, due to its high performance, reliability and flexibility.
# 
# 
# **Urllib**: BeautifulSoup does not fetch the web page for us. To do this, we'll rely on the [Urllib](https://docs.python.org/3.7/library/urllib.html#module-urllib) module available in the Python Standard Library, that implements classes and functions which help in opening URLs (authentication, redirections, cookies and so on). We will see another option, **requests**, below.

# In[1]:


import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup


# #### Retrieve and Parse an HTML page
# 
# `urllib.request.urlopen()` allows us to retrieve our target HTML page:

# In[2]:


html = urlopen("http://www.pythonscraping.com/pages/page1.html")


# What if the page doesn't exist?

# In[3]:


try:
    html = urlopen("http://www.pythonscraping.com/pages/page.html")
except Exception as e:
    print(e)


# Well, let's handle this properly...

# In[4]:


try:
    html = urlopen("http://www.pythonscraping.com/pages/page.html")
except urllib.request.URLError as e:
    pass # code your plan B here
except urllib.request.URLError as e:
    raise # raise any other exception


# We use `BeautifulSoup()` in conjunction with `lxml` to parse out `html` page and store it in the Beautiful Soup format

# In[5]:


# you might need to to the following:
#!pip install lxml


# In[6]:


html = urlopen("http://www.pythonscraping.com/pages/page1.html")
soup_page1 = BeautifulSoup(html, "lxml")


# In[7]:


#Let's scrape another couple of pages we'll need in our examples
soup_page3 = BeautifulSoup(urlopen("http://www.pythonscraping.com/pages/page3.html"), "lxml")
soup_wap = BeautifulSoup(urlopen("http://www.pythonscraping.com/pages/warandpeace.html"), "lxml")


# #### Let's look at the nested structure of the page
# 
# The `prettify()` method allows us to have a look at the structure of the HTML page

# In[8]:


print(soup_page1)


# In[9]:


print(soup_page1.prettify())


# #### Let's play with a HTML tag
# 
# The notation `soup.<tag>` allows us to retrieve the content marked by a tag (opening and closing tags included)

# In[10]:


# note that the first "<div>" tag is nested two layers deep (html → body → div).
soup_page1.div


# If the text is the only thing you're interested into, well, the `soup.<tag>.string` method comes in handy:

# In[11]:


soup_page1.div.string


# The HTML markup generated by Beautiful Soup can be modified:

# In[12]:


# let's change the content of our div
soup_page1.div.string = "this content has been changed"
# let's change the name of the tag
soup_page1.div.name = "new_div"


# In[13]:


print(soup_page1.prettify())


# In its simplest use, the `find()` method is an alternative to the `soup.<tag>` notation...

# In[14]:


soup_page1.find("new_div")


# In[15]:


soup_page1.new_div


# ...but this function allows for the searching of nodes by exploiting cues in the markup, such as a given **class attribute** value:

# In[16]:


print(soup_wap.prettify())


# In[17]:


soup_wap.find("span", attrs = {"class":"green"})


# The values of an attribute for a given tag instance can be retrieved by using the `get("ATTRIBUTE")` method. For instance, if we want to retrieve the URL of an image we can extract the `src` value from the corresponding `<img>` tag:

# In[18]:


soup_page3.img.get("src")


# If we want to know all the attibutes associated with a given tag, the `attrs` method is convenient:

# In[19]:


soup_page3.img.attrs


# In[20]:


# by returning a dictionary, it is easy to see how "attrs" can be used as an alternative to "get()"
soup_page3.img.attrs["src"]


# In[21]:


# if you fancy another way to do the same thing...
soup_page3.img["src"]


# #### Dealing with multiple HTML tags at once
# 
# When the same tag is used multiple time in the same page, however, both the `soup.<tag>` notation and the `find()` method allow you to access **only one instance** (i.e. the first):

# In[22]:


print(soup_wap.prettify())[180:1190]


# In[23]:


soup_wap.span


# In order to extract the **sequence of all the instances of a tag** in a file, we can use the `find_all()` method (previously known as `findAll()` and `findChildren()` in BS 3 and BS 2, respectively)

# In[24]:


soup_wap.find_all("span")


# The `find_all()` method as well allows for  the extraction of  all tags by exploiting cues in the markup, such as a given **class attribute** value:

# In[25]:


soup_wap.find_all("span",  attrs = {"class":"green"})


# ### Web Crawling
# 
# Web Crawlers are softwares designed to collect pages from the Web. In essence, they recursively implement the following steps: 
# 
# - they start by retrieving the page content for an URL 
# 
# 
# - they then parse it to retrieve other URLs of interest
# 
# 
# - they then focus on these new URLs, for each of which they repeat the whole process, ad infinitum

# For instance, if you want to crawl and **entire site**:
# 
# - start with a top-level page
# 
# 
# - parse the page (retrieve the data your application need) and extract all the internal links, by ignoring already visited URLs
# 
# 
# - for each new link, move to the corresponding page and repeat the previous step

# #### A Random walk through Wikipedia

# Let's set our starting page URL, fetch it and parse its HTML:

# In[26]:


starting_page = urlopen("https://en.wikipedia.org/wiki/Chris_Cornell")
soup = BeautifulSoup(starting_page, "lxml")


# At this point, it should be easy to extract all the links in the page:

# In[27]:


# links are defined by <a> tag
for link_element in soup.find_all("a")[:10]:
    print(link_element)


# Let's ignore all the "a" tags without an "href" attribute:

# In[28]:


for link_element in [tag for tag in soup.find_all("a") if 'href' in tag.attrs][:10]:
    
    url = link_element.attrs['href']
    
    print(url)


# Wikipedia is full of sidebar, footer, and header links that appear on every page, along with links to the category pages, talk pages, and other pages that do not contain different articles:
# 
# ```
# /wiki/Template_talk:Chris_Cornell
# ```
# 
# ```
# #cite_note-147
# ```
# 
# Moreover, we don't want to visit pages outside of Wikipedia:
# 
# ```
# http://www.chriscornell.com/
# ```

# Relevant links have three thing in common:
# 
# - they reside within the `div` with the `id` set to `bodyContent`
# 
# 
# - the URLs do not contain semicolons
# 
# 
# - the URLs begin with `/wiki/`

# In[29]:


import re

re_pattern = re.compile(r"^(/wiki/)((?!:).)*$")

body = soup.find("div", {"id": "bodyContent"})

for link in body.find_all("a", {'href': re_pattern}):

    print(link.attrs['href'])


# This code returns the list of all the Wikipedia articles linked to our starting page. 
# 
# This is not enough, we want to be recursively repeat this process for all these links. That is, we need a function that takes as input a Wikipedia article URL of the form `/wiki/<Article_Name>` and returns a list of all linked articles

# In[30]:


def get_links(article_url):
    """
    Retrieve all URLs on an English Wikipedia article page (e.g. /wiki/Amsterdam).
    
    This function needs a relative URL on the 
    http://en.wikipedia.org domain, such as '/wiki/Amsterdam'. 
    
    Args:
        article_url (str): URL of a website
        
    Returns:
        bs4.element.ResultSet: bs link elements resultset
        
    """
    
    page = urlopen("http://en.wikipedia.org" + article_url)
    soup = BeautifulSoup(page, "lxml")
    
    body = soup.find("div", {"id":"bodyContent"})
    
    re_pattern = re.compile(r"^(/wiki/)((?!:).)*$")
    
    links = body.find_all("a", href=re_pattern)
    
    return links


# Let's test our function by calling it in a script that randomly select, for each iteration, a random link and that stops after 10 URLs have been retrieved (or when it bumps into a page without link):

# In[31]:


import random

links = get_links("/wiki/Chris_Cornell")

for _ in range(10):  # for testing purposes, we want to do this 10 times
    if len(links) > 0:
        new_article = links[random.randint(0, len(links)-1)].attrs["href"]
        print(new_article)
        
        links = get_links(new_article)
        
    else:
        print("No links in this page!")
        break


# ---

# ### Exercise 1.
# 
# Write code to retrieve the **motto in English** (if the University has one) of the Internationally Ranked Universities in the Netherlands by starting from the following Wikipedia article:
# 
# https://en.wikipedia.org/wiki/List_of_universities_in_the_Netherlands

# In[32]:


# Your code here


# ---

# ## Working with APIs
# 
# An **Application Programming Interface** is a set of protocols that defines how software programs communicate among eachother. Without APIs, we have to scrape the Web or get the data directly. With APIs, we often can get structured data: it is a much more convenient way to work.
# 
# APIs are a great option in that they implement extensively tested routines (**high reliability**). However, you should spend time in learning how they work and, in some cases, they don't allow you to access the piece of information you may need (**low flexibility**).

# In[33]:


import requests  # External package: https://requests.readthedocs.io/en/master/


# In[34]:


# Example of a Google search


# In[35]:


query = "Tesla"
r = requests.get('https://www.google.com/search', params={'q': query})


# In[36]:


r.status_code


# In[37]:


print(r.headers['content-type'])
print(r.encoding)
print(r.url)


# In[38]:


r.text[:1000]


# ---

# ### Exercise 2.
# 
# 1. Inspect the Google search results page and understand how results are displayed.
# 
# 
# 2. Use BeautifulSoup to get the link of the first 10 results of this search out.

# ---

# What about using `requests` to query APIs? Easy using the param dictionary. Responses then follow the starndard format of the API (or you can request the one you like if available).

# In[39]:


r = requests.get('https://api.github.com')

# raw
r.content


# In[40]:


# json
r.json()


# ### Twitter API (OPT)
# 
# Two main APIs:
# 
# * **Streaming API**: a sample of public tweets and events as they published on Twitter, provides only real-time data without limits.
# 
# 
# * **REST API**: allows to search, follow trends, read author profile and follower data, post / modify. It provides historical data up to a week (for the free account, more by paying), requires a one-time request and has rate limit (varies for different requests and subscriptions).
# 
# 
# REST APIs (it is a style for developing Web services which is widely used): https://en.wikipedia.org/wiki/Representational_state_transfer
# 
# Some more basic info: https://developer.twitter.com/en/docs/basics/things-every-developer-should-know
# 
# Tutorials: https://developer.twitter.com/en/docs/tutorials

# #### Using the API: authentication
# 
# **For this part, you will need credentials from the Twitter dev website.**
# 
# A good way to store your keys is using `.conf` files and `configparser`.

# In[41]:


import configparser
config = configparser.ConfigParser()
config.read("stuff/conf.conf")


# In[42]:


config['twitter']['api_key']


# In[43]:


config['twitter']


# This is how my `conf.conf` file looks like (also in `stuff/conf_public.conf`):
# 
# ```
# [twitter]
# api_key = YOURS
# api_secret_key = YOURS
# access_token = YOURS
# access_secret_token = YOURS
# ```

# #### A useful package: Tweepy
# 
# https://tweepy.readthedocs.io/en/latest/index.html

# In[44]:


import tweepy


# In[45]:


# Tweepy Hello World

# authentication (OAuth)
auth = tweepy.OAuthHandler(config['twitter']['api_key'], config['twitter']['api_secret_key'])
auth.set_access_token(config['twitter']['access_token'], config['twitter']['access_secret_token'])

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets[:5]:
    print(tweet.text)


# #### Interlude: JSON
# 
# The Twitter API returns data structured in the JSON format. [JSON](https://www.json.org) (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. **It is basically a list of nested Python dictionaries.**
# 
# 
# Minimal example:
# 
# ```json
# {
#   "firstName": "John",
#   "lastName": "Doe",
#   "age": 21
# }
# ```
# 
# Extended example:
# 
# ```json
# {
#   "$id": "https://example.com/person.schema.json",
#   "$schema": "http://json-schema.org/draft-07/schema#",
#   "title": "Person",
#   "type": "object",
#   "properties": {
#     "firstName": {
#       "type": "string",
#       "description": "The person's first name."
#     },
#     "lastName": {
#       "type": "string",
#       "description": "The person's last name."
#     },
#     "age": {
#       "description": "Age in years which must be equal to or greater than zero.",
#       "type": "integer",
#       "minimum": 0
#     }
#   }
# }
# ```
# 
# 
# Online viewer: http://jsonviewer.stack.hu

# #### Using the API: search
# 
# All the most recent Tweets from a given hashtag.

# In[46]:


# queries

tweets = tweepy.Cursor(api.search, q="#nlproc")

for item in tweets.items(2):
    print(item._json)


# In[47]:


# queries with Boolean operators
import json

tweets = tweepy.Cursor(api.search, q="#nlproc")

for item in tweets.items(2):
    print(json.dumps(item._json, indent=4, sort_keys=False))


# #### Using the API: users
# 
# Get some info on a given user, and explore their friends/followers.

# In[48]:


user = api.get_user("elonmusk")

print("User:", user.screen_name)
print("------")
print("Friends:", user.friends_count)
print("Followers:", user.followers_count)
print("------")
for friend in user.friends(count=10):
    print(friend.screen_name)
print("------")
for friend in user.followers(count=10):
    print(friend.screen_name)


# #### Using the API: tweets from user

# In[49]:


user = api.get_user("elonmusk")
elon_tweets = user.timeline()

for tweet in elon_tweets[:10]:
    print(tweet.text)


# ---

# For those who don't have a Twitter account and app, here are some tweets on and by Boris Johnson!

# In[50]:


def get_mention_tweets(username, n=100):
    """
    Get all tweet mentions by Twitter username.
    
    Args:
        username (str): Twitter username
        n (int, optional): number of tweets to get from timeline
        
    Returns:
        list: List of tweets (str) in which this user is mentioned
    """
    
    if username.startswith('@'):
        user = username
    else:
        user = '@' + username
    
    mentions = []
    tweets_on_user = tweepy.Cursor(api.search, q=user, tweet_mode="extended")
    
    for tweet in tweets_on_user.items(n):
        mentions.append(tweet.full_text)
        
    return mentions
    
    
def get_user_tweets(username, n=100):
    """
    Get a user's tweets by username.
    
    Args:
        username (str): Twitter username
        n (int, optional): number of tweets to get from timeline
        
    Returns:
        list: List of tweets (str) from this user
    """
    
    user = api.get_user(username, tweet_mode="extended") # extended tweetmode gets also the longer 280/char tweets
    tweets_from_user = user.timeline(count=n)

    tweets = []
    for tweet in tweets_from_user:
        tweets.append(tweet.text)
        
    return tweets


# In[51]:


on_boris = get_mention_tweets("BorisJohnson")
from_boris = get_user_tweets("BorisJohnson")


# In[52]:


# Save to file (a one-column CSV)
f_on_boris = "stuff/tweets_on_boris.csv"
f_from_boris = "stuff/tweets_from_boris.csv"

# note we are using the "" as text delimiter
with open(f_on_boris, "w", encoding='utf-8') as f:
    for t in on_boris:
        f.write('"' + t + '"\n')
        
with open(f_from_boris, "w", encoding='utf-8') as f:
    for t in from_boris:
        f.write('"' + t + '"\n')


# ### Exercise 3.
# 
# 1. Download the last 100 (or another number) tweets mentioning a user you are interested into and the last 100 from the user itself. Alternatively, use the tweets in the on_boris and from_boris files.
# 
# 
# 2. Create a minimal pipeline to normalize the tweets into lists of tokens.
# 
# 
# 3. Count and compare from the two datasets, the most frequent (top 10):
#     - tokens
#     - hashtags
#     - other user mentions

# In[53]:


# Your code here


# In[ ]:




