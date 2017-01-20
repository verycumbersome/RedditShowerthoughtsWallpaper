import sys
import math
import getpass
import re
import os
import random
import requests

try:
    import praw
except:
    lib = "PRAW"
    print "ImportError: %s is not found on your system" % (lib)
    print "You must install %s to operate this program" % (lib)
    sys.exit()

r = praw.Reddit(user_agent="JustDudeStuff_V1",client_secret="joK9SvU32QYtxZHz_dN_ecn4Bo8",client_id="BWVD4XaKSFT8Hg")

# def login():
#     r.login("justbotstuff", "Matthewunited1")

def GetTopSubmissions(text_subreddit, image_subreddit, l):
    SubredditPic = r.subreddit(image_subreddit)
    SubredditText = r.subreddit(text_subreddit)

    PicContent = SubredditPic.top(limit = l)
    TextContent = SubredditText.top(limit = l)

    PicList = [sub for sub in PicContent]
    TextList = [sub for sub in TextContent]

    imgURL = PicList[random.randint(0, l - 1)].url
    Text = TextList[random.randint(0, l - 1)].title

    return imgURL, Text
