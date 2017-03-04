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
from difflib import SequenceMatcher
# Create your views here.


def home(request):
	return render (request,'index.html')


def graphs(request):
	tweets_data_path = 'tweepy/anusha.txt'
	tweets_data = []
	location_list = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
	    try:
	        tweet = json.loads(line)
	        tweets_data.append(tweet)
	    except:
	        continue
	print len(tweets_data)
	for total in range(len(tweets_data)):
		if tweets_data[total]['user']['location']:
			found_locations = Event_tweet_data.objects.values_list("event_location")
			location_list_array = tweets_data[total]['user']['location']
			location_list_array = location_list_array.split(',')
			for x in location_list_array:
				location_list.append(x)
			if len(found_locations) == 0:
				print 'found location is none'
				tweet_object = Event_tweet_data()
				tweet_object.event_location = tweets_data[total]['user']['location']
				tweet_object.event_count = 0
				tweet_object.save()
			for x in found_locations:
				flag = True
				for y in location_list_array:
					print 'X'+ x
					print 'Y'+ y
					similarity = SequenceMatcher(a=x,b=y).ratio() * 100
					if similarity > 99 and flag:
						match_location = Event_tweet_data.objects.get(event_location = y)
						match_location.event_count += 1
						match_location.save() 
						flag= False
						break
				if flag:
					print 'hello'
					tweet_object = Event_tweet_data()
					tweet_object.event_location = tweets_data[total]['user']['location']
					tweet_object.event_count = 0
					tweet_object.save()
	return HttpResponse(location_list)