import os
import praw
from dotenv import load_dotenv
from tqdm import tqdm
import pandas as pd

load_dotenv()

reddit = praw.Reddit(client_id=os.environ.get("REDDIT_API_KEY"),
                     client_secret=os.environ.get("REDDIT_API_SECRET"),
                     user_agent='python:co.guitton.topfootball:v1.0 (by u/laguitte)')

if __name__ == "__main__":
    records = []
    # Reddit API terms imply to wait 2 seconds between each API call
    for submission in tqdm(reddit.domain('onefootball.com').top(limit=300)):
        # https://praw.readthedocs.io/en/latest/code_overview/models/submission.html
        subreddit = submission.subreddit
        records.append(dict(
            created_at_utc=submission.created_utc,
            submission_id=submission.name,
            num_comments=submission.num_comments,
            score=submission.score,
            subreddit_id=subreddit.name,
            subreddit_name=subreddit.display_name,
            subreddit_subscribers=subreddit.subscribers,
            title=submission.title,
            upvote_ratio=submission.upvote_ratio,
            article_url=submission.url,
            submission_url=submission.permalink
            )
        )

    df = pd.DataFrame.from_records(records)
    df["created_at_utc"] = pd.to_datetime(df.created_at_utc, unit='s')

    df.to_csv('data/year=2020/month=03/day=01/top.csv')
