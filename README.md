# Reddit Comment Scraper Bot (using PRAW)

A Python bot that uses the PRAW library to fetch and process comments from a specific Reddit post. It allows you to access and extracts the comments on a specific Reddit post, including the comment itself, comment author, comment id and comment score (number of upvotes that comment has).

---
## What is PRAW

PRAW is short for "Python Reddit API Wrapper". It makes accessing Reddit's server relatively quicker by handling the HTTP requests
and parsing the data from the API into objects you can manipulate.
PRAW simply makes requests on your behalf to Reddit's server, then converts the data it gets back into what you can work with.
We are going to use PRAW to build our Reddit bot. Let's go!

------------------------------------------------------------------------------------------
### Install PRAW

`pip install praw`

------------------------------------------------------------------------------------------
### Create your Reddit bot

1. Go to Reddit's [App Preferences](https://www.reddit.com/prefs/apps) page.
2. Click "Are you a developer? Create an app..."
3. Fill out the following:
- Give your bot a name
- Select between web app, installed app or script. For this case, we're using a script
- Briefly describe your bot
- about url - This is a link where people can learn more about your bot. You can leave this blank if you don't have one.
- redirect url- This is the URL where users will be sent after they log in to Reddit to use your app. Since our script is locally hosted, we use http://localhost/ to send us back to our own computer.
4. Click create app
5. After that, you'll get your client id and secret to be used in praw.

------------------------------------------------------------------------------------------
### Import PRAW (After installing it)

Either you do a.
`import praw`

Or you do b.
`from praw import reddit`

for simplicity, let's stick with a.

------------------------------------------------------------------------------------------
### Authenticate with credentials

These credentials will be given to you when you create the bot.
```
reddit = praw.Reddit(
    client_id="[Put id here]",
    client_secret="[Put secret here]",
    user_agent="[Insert bot name here] by /u/[your username]"
)
```
------------------------------------------------------------------------------------------
### Fetch the post you want to use using the link of the post
```
url_of_post = "[Insert post link here]"
sub = reddit.submission(url=url_of_post)
```
------------------------------------------------------------------------------------------
### Load all the comments using replace_more(limit=None)

`sub.comments.replace_more(limit=None)`

Note:

`limit=None` - Removes every instance of "Load more comments"

`limit=0` - Removes the first instance of "Load more comments"

`limit=1` - Removes the first 2 instances of "Load more comments"

`limit=10` - Removes the first 10 instances of "Load more comments" (if it has up to that)

------------------------------------------------------------------------------------------
### Print the first 10 comments in a numbered list
```
for index, comment in enumerate(sub.comments.list()[:10], start=1):
    print(f"{index} - {comment.body}")
```
------------------------------------------------------------------------------------------

ENJOY!

D.
