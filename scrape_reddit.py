from fuzzywuzzy import process
import praw
import time

reddit = praw.Reddit(
    "houseplantimagebot",
    user_agent="my user agent"
)

for submission in reddit.subreddit("houseplants").top("year", limit=10):
    time.sleep(.5)

    # skip non-image posts
    if not submission.url.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        continue

    result = process.extractOne(submission.title.lower(),["string of dolphins", "desert cactus"])
    print(result)

    print(submission.title)
    print(submission.url)