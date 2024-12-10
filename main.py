# Install library
import praw

# Authenticate with the following credentials
reddit = praw.Reddit(
    client_id="[Put client id here]",
    client_secret="[Put client secret here]",
    user_agent="[Insert bot name here] by /u/[your username]"
)

# Fetch the post
url_of_post = "[Insert url of the post here]"
sub = reddit.submission(url=url_of_post)

# This loads ALL the comments on that post
sub.comments.replace_more(limit=None)

# Print the first 10 comments in a numbered list
for index, comment in enumerate(sub.comments.list()[:10], start=1):
    print(f"{index} - {comment.body}")
