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


class User(Document):
    """A User document that aims to mirror most of the API specified by Django
    at http://docs.djangoproject.com/en/dev/topics/auth/#users
    """
    _id = StringField()
    username = StringField(max_length=30, required=True)

    first_name = StringField(max_length=30)

    last_name = StringField(max_length=30)
    email = EmailField(max_length=200)
    password = StringField(max_length=128)
 
    last_login = DateTimeField()
    date_joined = DateTimeField()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def set_password(self, raw_password):
        """Sets the user's password - always use this rather than directly
        assigning to :attr:`~mongoengine.django.auth.User.password` as the
        password is hashed before storage.
        """
        self.password = make_password(raw_password)
        self.save()
        return self

    def check_password(self, raw_password):
        """Checks the user's password against a provided password - always use
        this rather than directly comparing to
        :attr:`~mongoengine.django.auth.User.password` as the password is
        hashed before storage.
        """
        return check_password(raw_password, self.password)

