from django.shortcuts import render
from apps.testingmongo.models import Poll, Choice
from mongoengine import *
from apps.testingmongo.models import *
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth import authenticate
from django.http import *
from django.contrib.auth import login,  logout
import datetime
import json
# Create your views here.


def home(request):
	return render (request,'index.html')


def graphs(request):
	tweets_data_path = 'anusha.txt'
	tweets_data = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
	    try:
	        tweet = json.loads(line)
	        tweets_data.append(tweet)
	    except:
	        continue
	print len(tweets_data)
	for total in range(len(tweets_data)):
		print tweets_data[total]['user']['location']
	return render (request, 'index.html')