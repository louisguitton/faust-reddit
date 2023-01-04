```bash
curl https://www.reddit.com/api/v1/access_token --user-agent "linux:reddit_alerts:v0.1.0 (by /u/laguitte)" --user VtPfjSBrPKTznA:XGfdb_OeCArySronx4o0jvE-4RQ --data 'grant_type=client_credentials'
```

```bash
litecli foo.db
```

```python
def print_submission(submission):
    print("A new reddit submission")
    print("{} is being discussed on /r/{}".format(
        submission.title,
        submission.subreddit.display_name
        ))
    print("So far there has been {} comments since it was posted {}".format(
        submission.num_comments,
        arrow.get(submission.created_utc).humanize()
        ))
    print("\n")
```
