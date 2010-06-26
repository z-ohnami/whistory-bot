import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

#import logging
from twitbot import TwitBot

class TweetAction(webapp.RequestHandler):
    def __init__(self):
        twit = TwitBot()
        self.action = {
#            'friends'   : twit.friends,
#            'followers' : twit.followers,
#            'friendship': twit.friendship,
            'update'    : twit.update,
        }

    def get(self):
        action = self.action.get(self.request.get('action'))
        if action:
            action()        
        template_values = {
            'actions' : sorted(self.action.keys()),
            'done'    : self.request.get('action'),
            'path'    : self.request.path,
            }
        path = os.path.join(os.path.dirname(__file__), 'template.html')
        self.response.out.write(template.render(path, template_values))

class MainPage(webapp.RequestHandler):
        
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'main.html')
        self.response.out.write(template.render(path, {}))


application = webapp.WSGIApplication([('/', MainPage),('/bot_action', TweetAction)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

