import datetime
import pytz
import praw
import os
import random

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
user_agent = os.environ.get('USER_AGENT')
reddit_username = os.environ.get('REDDIT_USERNAME')
reddit_password = os.environ.get('REDDIT_PASSWORD')

# Get the current date and time in UTC
current_utc_datetime = datetime.datetime.utcnow()

# Convert UTC time to the India Standard Time (IST) timezone
ist = pytz.timezone('Asia/Kolkata')
ist_datetime = current_utc_datetime.astimezone(ist)
today_date = ist_datetime.strftime("%d %B, %Y")

# Get the title of the post
post_title = ("Late Night Random Discussion Thread - " + today_date)

reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        username=reddit_username,
        password=reddit_password,
    )

# Specify the subreddit where the post is located
subreddit = reddit.subreddit('IndiaSocial')

# Get the post ID
posts = subreddit.search(post_title, limit=1)
for post in posts:
    post_id = post.id

comments = ["Upvote this thread to make this cat happy ![gif](giphy|5LU6ZcEGBbhVS)", "Remember to upvote the thread!!!!!", "Upvote the thread gois ❤️", "Upvote the thread *and* me cutus 🥰😍"]
comment_text = random.choices(comments)

# Post the comment
submission = reddit.submission(id=post_id)
submission.reply(comment_text)
