import utils
import time
import re

import config_parse

class Earthporn_ShowerThoughts:
    def __init__(self):
        args = config_parse.get_args()
        self.args = args

        self.text_subreddit = self.args["text_subreddit"]
        self.image_subreddit = self.args["image_subreddit"]
        self.top_limit = self.args["top_limit"]
        self.refresh_rate = self.args["refresh_rate"]


#    def run_program(self):
        while(True):
            RedditPic, RedditText = utils.GetTopSubmissions(self.text_subreddit, self.image_subreddit,self.top_limit)

            with open('/Users/matthewjordan/git/Earthporn_ShowerThoughts/html/Template.html', 'r') as f: template = f.read()
            with open('/Library/WebServer/Documents/index.html', 'w') as f: f.write(template.decode("utf8").format(RedditPic, RedditText))
            print RedditPic, RedditText

            time.sleep(self.refresh_rate)
