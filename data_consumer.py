import boto3

kinesis_client = boto3.client("kinesis")


response = kinesis_client.describe_stream(
    StreamName='reddit.soccer',
)
shard = response['StreamDescription']["Shards"][0]

response = kinesis_client.get_shard_iterator(
    StreamName='reddit.soccer',
    ShardId=shard["ShardId"],
    ShardIteratorType='AT_SEQUENCE_NUMBER',
    StartingSequenceNumber=shard["SequenceNumberRange"]["StartingSequenceNumber"]
)
iterator = response["ShardIterator"]

response = kinesis_client.get_records(
    ShardIterator=iterator,
)
iterator = response["NextShardIterator"]
records = response["Records"]
