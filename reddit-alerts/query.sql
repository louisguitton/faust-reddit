Select
  date_at,
  title,
  subreddit,
  num_comments,
  created_at_utc
From
  submissions
Where
  date_at between DATETIME('now', '-1 hour')
  and DATETIME('now');
