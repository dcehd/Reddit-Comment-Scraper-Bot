# Reddit Comment Scraper Bot (using PRAW)

A Python bot that uses the PRAW library to fetch and process comments from a specific Reddit post.. With this bot, you can access and extract detailed information about the comments, including:

- The comment text
- The comment author
- The comment ID
- The comment score (upvotes)

---

## What is PRAW?

PRAW is short for **Python Reddit API Wrapper**. It simplifies interactions with Reddit's API by handling HTTP requests and converting API responses into Python objects that are easy to manipulate.

Essentially, PRAW acts as a bridge between your Python code and Reddit’s servers, enabling you to seamlessly retrieve and work with Reddit data.

We’ll be using PRAW to build our Reddit bot. Let’s get started!

---

## Installation

First, install the PRAW library via pip:

```
pip install praw

```

---

## Create Your Reddit Bot

To get started, you’ll need to create a bot through Reddit’s developer tools. Here’s how:

1. Go to Reddit’s [App Preferences](https://www.reddit.com/prefs/apps) page.
2. Click **"Are you a developer? Create an app..."**.
3. Fill out the form:
    - **Name:** Give your bot a unique name.
    - **App Type:** Select "Script."
    - **Description:** Briefly describe your bot’s purpose.
    - **About URL:** This is a link where people can learn more about your bot. You can leave this blank if you don't have one.
    - **Redirect URL:** This is the URL where users will be sent after they log in to Reddit to use your app. Since our script is locally hosted, we use `http://localhost/`.
4. Click **Create App**.
5. Note down your **Client ID** and **Client Secret** – you’ll need them to authenticate your bot.

---

## Import PRAW

To use PRAW in your script, you can either:

**Option A:**

```
import praw

```

**Option B:**

```
from praw import Reddit

```

We’ll stick with Option A for simplicity.

---

## Authenticate Your Bot

Using the credentials we got when we created the bot, authenticate as follows:

```
reddit = praw.Reddit(
    client_id="[Put id here]",
    client_secret="[Put secret here]",
    user_agent="[Insert bot name here] by /u/[your username]"
)

```

---

## Fetch the Target Reddit Post

Provide the URL of the Reddit post you want to scrape:

```
url_of_post = "[Insert post link here]"
sub = reddit.submission(url=url_of_post)

```

---

## Load All Comments

Use the `replace_more` method to load all comments:

```
sub.comments.replace_more(limit=None)

```

**Note:**

- `limit=None`: Removes all instances of "Load more comments."
- `limit=0`: Removes only the first instance of "Load more comments."
- `limit=1` - Removes the first 2 instances of "Load more comments".
- ...
- `limit=10` - Removes the first 10 instances of "Load more comments" (if it has up to that).

---

## Print the First 10 Comments

Here’s how to display the first 10 comments in a numbered list:

```python
for index, comment in enumerate(sub.comments.list()[:10], start=1):
    print(f"{index} - {comment.body}")

```

---

## Conclusion

With this bot, you can effortlessly access and analyze comments from Reddit posts for various use cases, from data analysis to personal projects.

Enjoy building your Reddit bot with PRAW!
