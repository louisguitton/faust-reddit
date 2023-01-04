#!/usr/bin/env python

import os

import boto3
import praw
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.environ.get("REDDIT_API_KEY"),
    client_secret=os.environ.get("REDDIT_API_SECRET"),
    user_agent="python:co.guitton.topfootball:v1.0 (by u/laguitte)",
)


kinesis_client = boto3.client("kinesis")


def main():
    for comment in reddit.subreddit("soccer").stream.comments():
        print(comment)
        kinesis_client.put_record(
            StreamName="reddit.soccer", Data=comment.body, PartitionKey=comment.id
        )

    # for submission in reddit.subreddit('soccer').stream.submissions():
    #     print(submission)

if __name__ == "__main__":
    main()
