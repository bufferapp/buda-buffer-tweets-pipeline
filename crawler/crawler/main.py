#!/usr/bin/python

import tweepy
import os
import json
import logging
from google.cloud import pubsub
from boltons.iterutils import remap

logger = logging.getLogger()
logger.setLevel(logging.INFO)

access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')


class TweetCrawler():
    def __init__(self, api, track_filters, producer, validations={}):

        self.producer = producer
        self.validations = validations
        self.track_filters = track_filters

        listener = BufferTweetsStreamListener(crawler=self)
        self.stream = tweepy.Stream(auth=api.auth, listener=listener)
        self.stream.filter(track=track_filters)

    def handle_tweet(self, tweet):
        if self.validate_tweet(tweet):
            tweet_json = tweet._json
            tweet_json = self.cleanup_tweet(tweet_json)
            self.producer.publish(json.dumps(tweet_json))

    def cleanup_tweet(self, tweet):
        return remap(tweet, visit=lambda p, key, value: key != 'bounding_box')

    def validate_tweet(self, tweet):
        for mention in self.validations.get('mentions', []):
            if self.has_mention(tweet, mention):
                return True

        for hashtag in self.validations.get('hashtags', []):
            if self.has_hashtags(tweet, hashtag):
                return True

        return False

    def has_mention(self, tweet, mention):
        for m in tweet.entities.get('user_mentions', []):
            if mention == m['screen_name']:
                return True
        return False

    def has_hashtags(self, tweet, hashtag):
        for h in tweet.entities.get('hashtags', []):
            if hashtag == h['text']:
                return True
        return False


class PubSubProducer():
    def __init__(self, project_id, topic_name, client=None):
        self.topic = f'projects/{project_id}/topics/{topic_name}'
        if client is None:
            client = pubsub.PublisherClient()
        self.client = client

    def publish(self, data):
        logger.info(f'Publishing data to {self.topic}')
        data = data.encode('utf-8')
        self.client.publish(self.topic, data)


class BufferTweetsStreamListener(tweepy.StreamListener):
    def __init__(self,  crawler, **args):
        super(BufferTweetsStreamListener, self).__init__(**args)
        self.crawler = crawler

    def on_status(self, status):
        if self.crawler:
            self.crawler.handle_tweet(status)
        return status

    def on_error(self, status_code):
        # https://developer.twitter.com/en/docs/basics/response-codes
        print(status_code)


def run(argv=None):
        auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        buffer_producer = PubSubProducer('buffer-data', 'buffer-tweets')
        buffer_crawler = TweetCrawler(api, ['#bufferchat', '#buffer', 'buffer'],
                                    buffer_producer,
                                    validations={
                                        'mentions': ['buffer'],
                                        'hashtags': ['buffer', 'bufferchat']
                                    })

