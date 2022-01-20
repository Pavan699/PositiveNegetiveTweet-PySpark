'''
@Author: Pavan Nakate
@Date: 2021-01-12 8:30
@Last Modified by: Pavan Nakate
@Last Modified time: 2021-01-12
@Title : SQL-Server-Connection
'''
import csv
import time
import tweepy
from  textblob import TextBlob 

consumer_key= 'KOs4rVDZR9dIyFtYTYgtbLf9w'
consumer_secret= 'UMpqRZVOtfdNon7rALNWSXikwVG6SHSqYitRw9ghKQzh4ZvEjs'
access_token= '1312638419365851139-TfFsFzNTdsSajpelQEqjVeObOyn2iU'
access_token_secret= 'XRbS4CuDDqE18YUnPdhqR8XnJwbkNjKL8schKeAyYJX7M'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

tweet_search = api.search_tweets('Lord Shardul')

pos='positive'
neg='negative'
positive_count=0
negative_count=0

header = ["pos","neg","positive_count","negative_count"]
try:
   with open('tweets.csv', 'w') as csv_file:
         csv_writer = csv.DictWriter(csv_file, fieldnames=header)
         csv_writer.writeheader()

   while True:
   # printing line by line
      with open('tweets.csv', 'a') as csv_file:
          
         for tweet in tweet_search:
            print(tweet.text)
            analysis=TextBlob(tweet.text) 
            print(analysis.sentiment)
           
            if analysis.sentiment.polarity > 0:
               print("positive")
               positive_count = positive_count + 1
            elif analysis.sentiment[0]<0:
               print("Negative")
               negative_count = negative_count + 1
            else :
               print("Neutral")

            csv_writer = csv.DictWriter(csv_file, fieldnames=header)
            details = {
                     "pos": pos,
                     "neg": neg,
                     "positive_count":positive_count,
                     "negative_count":negative_count
                     }
            csv_writer.writerow(details)
            time.sleep(1) 
            print(positive_count,negative_count)

except Exception as e:
   print(e)