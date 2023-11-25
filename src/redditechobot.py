import datetime
import pytz
import praw
import os

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

# Calculate yesterday's date
yesterday_datetime = ist_datetime - datetime.timedelta(days=1)
yesterday_date = yesterday_datetime.strftime("%d %B, %Y")

# Get the title of the post
post_title = ("Late Night Random Discussion Thread - " + yesterday_date)

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

comment_text = 'Gub moin Nimmo, iKR, Godfi, Cucu, Harpu, Mochi-san, Moody Barbie, Entcune, dariya, successful strain, biryani man, SkyDriver, Tony Gunk, Nanga Lafanga, motachondria, InjuryArtistic, RiyalCounter, greatest idiot, aadesh, YoursTrullii, Videshikaua, deep pudding, distressed doc, bossyblueberry, clarku, one punch man, nadaan parinda, prawns no more, chulbul pandey, 10xP, guy who talks, luna crest, brotherman rogue, kai_1100, cow_word, uppsak, tempu, sCams, its rain, itoohaveadream, ganymede, pristine rain, RAVENGRIMOIRE, jupiiiiiiii, bingua, cautious reading, prof dhokla, bear energy, sleepylazydumb, awwhoneyy, pikuuu_, cantthinkofaname231, chotuchaiwala, emty, lifeendon, zenith, greedyenthu, p_W_n. Ghyanks!'

# Post the comment
submission = reddit.submission(id=post_id)
submission.reply(comment_text)
