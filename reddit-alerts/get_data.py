import hashlib
import datetime
import praw
from marshmallow import Schema, fields
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = sa.create_engine("sqlite:///foo.db")
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


class Submission(Base):
    __tablename__ = "submissions"
    uuid = sa.Column(sa.String, primary_key=True)
    date_at = sa.Column(sa.DateTime)
    submission_id = sa.Column(sa.String)
    subreddit = sa.Column(sa.String)
    audience_size = sa.Column(sa.Integer)
    author_name = sa.Column(sa.String)
    created_at_utc = sa.Column(sa.DateTime)
    upvotes = sa.Column(sa.Integer)
    downvotes = sa.Column(sa.Integer)
    permalink = sa.Column(sa.String)
    num_comments = sa.Column(sa.Integer)
    title = sa.Column(sa.String)
    url = sa.Column(sa.String)
    domain = sa.Column(sa.String)

    def __repr__(self):
        return "<Submission(uuid={self.uuid!r})>".format(self=self)


Base.metadata.create_all(engine)


class SubmissionSchema(Schema):
    date_at = fields.Method('get_now')
    submission_id = fields.Str(attribute='id')
    subreddit = fields.Str(attribute='subreddit_name_prefixed')
    audience_size = fields.Int(attribute='subreddit_subscribers')
    author_name = fields.Method('get_author_name')
    created_at_utc = fields.Method('get_created_at')
    upvotes = fields.Int(attribute='ups')
    downvotes = fields.Int(attribute='downs')
    permalink = fields.Str()
    num_comments = fields.Int()
    title = fields.Str()
    url = fields.Url()
    domain = fields.Str()
    uuid = fields.Method('get_primary_key')

    def get_now(self, obj):
        return datetime.datetime.utcnow()

    def get_author_name(self, obj):
        return obj.author.name

    def get_created_at(self, obj):
        return datetime.datetime.fromtimestamp(obj.created_utc)

    def get_primary_key(self, obj):
        return hashlib.md5("{} {}".format(obj.created_utc, obj.id).encode('utf-8')).hexdigest()

    class Meta:
        model = Submission


def main():
    reddit = praw.Reddit('my_bot')
    submissions = reddit.domain('onefootball.com').hot(limit=10)

    schema = SubmissionSchema(many=True)
    result = schema.dump(submissions)

    objects = [
        Submission(**s) for s in result.data
    ]
    session.bulk_save_objects(objects)
    session.commit()


if __name__ == "__main__":
    main()
