import praw
import requests
import json

CLIENT_ID = "sBx6U_qoUZzelw"
SECRET = "y841Y85Zcsslxxj-UozcsFdoKwc"
AGENT = "Linux:Python.CoronaNews (by: ponkbrow)"


def test_reddit():
    """TODO: Docstring for test_reddit.
    :returns: TODO

    """
    return "working"


reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET,
                     user_agent="felipon_bot")


def til_random():
    """TODO: Docstring for til_random.
    :returns: A dictionary with a random fact and a url
    """
    todayilearned = reddit.subreddit('todayilearned')
    todayilearned.random()
    x = todayilearned.random()
    return {"title": x.title, "url": x.url}


def affirmations():
    """ Docstring for affirmations.
    :returns: un objeto json de el api de https://www.affirmations.dev/
    """
    url = "https://www.affirmations.dev/"
    aff = requests.get(url)
    return json.loads(aff.text)


if __name__ == "__main__":
    pass
