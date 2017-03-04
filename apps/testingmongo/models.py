from mongoengine import *
import datetime
from django.contrib.auth.hashers import check_password

class Choice(EmbeddedDocument):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)


class Poll(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(help_text='date published')
    choices = ListField(EmbeddedDocumentField(Choice))

class Event_tweet_data(Document):
    event_location = StringField(max_length=200)
    event_count = IntField(default=0)
