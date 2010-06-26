# -*- coding: utf-8 -*-
#import logging
import msg
import oauth
import yaml

class TwitBot:
    def __init__(self):
        # from config.yaml
        #  bot:
        #    CONSUMER_KEY: aaa
        #    CONSUMER_SECRET: bbb
        #    ACCESS_TOKEN: ccc
        #    ACCESS_TOKEN_SECRET: ddd
        config_data = yaml.load(open('./config.yaml'))
        self.bot_config = config_data['bot']

    def update(self, status = None, in_reply_to = None):
        if not status:
            status = msg.getMsg()

        client = oauth.TwitterClient(self.bot_config['CONSUMER_KEY'],self.bot_config['CONSUMER_SECRET'], None)
        param = {'status': status}
        client.make_request('http://twitter.com/statuses/update.json',
                            token=self.bot_config['ACCESS_TOKEN'],
                            secret=self.bot_config['ACCESS_TOKEN_SECRET'],
                            additional_params=param,
                            protected=True,
                            method='POST')


