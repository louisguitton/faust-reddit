# /r/soccer stream to ElasticSearch

- faust from Robinhood is great but requires a Kafka broker and doesn't support Kinesis
- Kinesis is easier to run in production but requires to use boto3 or the KCL

so either I go:

- AWS MSK + faust
- AWS Kinesis + boto3 (preferrable if I have 1 simple shard)


You can stream a subreddit comments or submissions
but not a domain 
