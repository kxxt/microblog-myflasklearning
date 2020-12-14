from pymongo import MongoClient


class DBHandler:
    def __init__(self, papp):
        self.client = MongoClient(papp.config.get('MONGODB_HOST'), papp.config.get('MONGODB_PORT'))
        self.db = self.client.microblog
        self.users = self.db.users
        self.posts = self.db.posts
        self.urels = self.db.urels
        self.comments = self.db.comments
