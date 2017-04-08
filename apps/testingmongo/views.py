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
from django.db.models import Q
import httplib, urllib
import socket
# Create your views here.


def home(request):
	return render (request,'index.html')


def graphs(request):
	tweets_data_path = 'data.txt'
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
				for item in location_list_array:
					print 'found location is none'
					tweet_object = Event_tweet_data()
					string = ''.join(e for e in item if e.isalnum())
					string = ''.join([i for i in string if not i.isdigit()])
					tweet_object.event_location = string.strip()
					tweet_object.event_count = 0
					tweet_object.save()
			else:
				for y in location_list_array:
					found_locations = Event_tweet_data.objects.values_list("event_location")
					flag = True
					for x in found_locations:
						print 'X'+ x
						print 'Y'+ y
						string = ''.join(e for e in y if e.isalnum())
						string = ''.join([i for i in string if not i.isdigit()])
						similarity = SequenceMatcher(a=x.strip(),b=string.strip()).ratio() * 100
						print similarity
						if similarity > 75 and flag or x in string:
							match_location = Event_tweet_data.objects.get(event_location=x)
							match_location.event_count += 1
							match_location.save() 
							flag= False
							break
					if flag:
						tweet_object = Event_tweet_data()
						string = ''.join(e for e in y if e.isalnum())
						string = ''.join([i for i in string if not i.isdigit()])
						tweet_object.event_location = string.strip()
						tweet_object.event_count = 1
						tweet_object.save()
	return HttpResponse(location_list)

def generate_graph(request):
	chunk = []
	total_list = []
	render_data = {}
	location_objects = Event_tweet_data.objects().values_list('event_location')
	count_objects = Event_tweet_data.objects().values_list('event_count')
	for item in range(len(location_objects)):
		chunk = []
		chunk.append(str(location_objects[item]))
		print str(location_objects[item])
		chunk.append(count_objects[item])
		total_list.append(chunk)
	render_data['graph_data'] = json.dumps(total_list)
	render_data['reach'] = 'Reach in Numbers'
	render_data['topic'] = 'Twitter Data analysis for Womens Day'

	return render(request,'graphs.html', render_data)

def geocoding(request):
	tweets_data_path = 'data.txt'
	tweets = []
	location_list = []
	tweets_file = open(tweets_data_path, "r")
	for line in tweets_file:
	    try:
	        tweets.append(json.loads(line))
	    except:
	        continue
	print len(tweets)
	for total in range(len(tweets)):
		if tweets[total]['user']['location']:
			address = tweets[total]['user']['location']
			print address;
			params = urllib.urlencode({'address': 'India', 'key': 'AIzaSyCz3r0CzBrK3xKrBvfPgHQCJcX51GzJSYQ'})
			headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
			conn = httplib.HTTPSConnection("maps.googleapis.com", 43)
			conn.request("POST", "/maps/api/geocode/json", params, headers)
			response = conn.getresponse()
			print response.status, response.reason
			responseData = json.loads(response.read())
			latitude = responseData[0]['results']['geometry']['location']['lat']
			longitude = responseData[0]['results']['geometry']['location']['lng']
			conn.close()
	return HttpResponse(responseData)