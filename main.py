from flask import Flask, render_template, request
import tweepy
import requests
import json
import os
key = os.environ['API_KEY']
client = tweepy.Client(bearer_token='{}'.format(key))
def get_tweet_interactions(tweet_link, winner):

#get tweet link from user
    tweet_id = tweet_link.split("/")[-1]
    print(tweet_id)
# get list of users who liked the tweet
    likes = []
    users = client.get_liking_users(id=tweet_id)
    for user in users.data:
        likes.append(user.username)
    print(likes)
# get list of users who retweeted the tweet
    retweets = []
    retweeters = client.get_retweeters(id=tweet_id)
    for retweet in retweeters.data:
        retweets.append(retweet.username)
    print(retweets)

# get list of users who commented on the tweet
    #comments = client.GetComments(tweet_id=tweet_id)
    #for user in comments:
     #   print(user.items())
       # comment.append(user.items())
    common_users = [x for x in likes if x in retweets]
    winner = winners(common_users, winner)
    return winner

import random
def winners(common_users, winner):
    n ='{}'.format(winner)
    a = []
    for i in range(int(n)):
        a.append(random.choice(common_users))
    return a 


# call the function to get the interactions on the tweet
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('name.html')
@app.route('/howdy', methods=['POST'])
def howdy():
    name = request.form['tweet']
    winner = request.form['winners']
    df = get_tweet_interactions(name, winner)
    return """
    <h1>Hello!!!!<h1>
    <h1>{}<h1>
    """.format(df)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=int(os.environ.get('PORT', 8080)))
