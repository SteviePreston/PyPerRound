from urllib import response
import requests as req
import pandas as pd
import feedparser as fp
import os

# get RSS Feeds function


def getRSSFeed(url):
    response = req.get_source(url)
    responseParse = fp.parse(url)
    title = responseParse.feed.title
    desc = responseParse.feed.description
    link = responseParse.feed.link
    pubDate = responseParse.feed.pubDate
    print(title, desc, link, pubDate)


# Fetch News Functions


def getDailyMail():
    getRSSFeed("https://www.dailymail.co.uk/news/index.rss")


def getBBCTech():
    getRSSFeed("http://feeds.bbci.co.uk/news/technology/rss.xml")


def getWallStJournal():
    getRSSFeed("https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml")


def getNasdaqCrypto():
    getRSSFeed("https://www.nasdaq.com/feed/rssoutbound?category=Cryptocurrencies")


def getNasdaqAI():
    getRSSFeed(
        "https://www.nasdaq.com/feed/rssoutbound?category=Artificial+Intelligence"
    )


# Change to the Working Directory


def ChDir2c():
    os.chdir("/Users/stevie/Developer/C/")
    print("I have changed Directories")


def ChDir2py():
    os.chdir("/Users/stevie/Developer/Python/")
    print("I have changed Directories")


def ChDir2react():
    os.chdir("/Users/stevie/Developer/JavaScript/React/")
    print("I have changed Directories")


def ChDir2node():
    os.chdir("/Users/stevie/Developer/JavaScript/Node/")
    print("I have changed Directories")


def ChDir2ai():
    os.chdir("/Users/stevie/Developer/Python/Tensorflow/")
    print("I have changed Directories")


def ChDir2java():
    os.chdir("/Users/stevie/Developer/Java/")
    print("I have changed Directories")
