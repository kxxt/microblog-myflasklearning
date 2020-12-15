from datetime import datetime
from hashlib import md5

from werkzeug.security import generate_password_hash, check_password_hash

import app

from .base.data_object import DataObject, db_property
from ..query import BaseQuery


class User(DataObject):
    def __init__(self, username, passwd, email, query, friendly_name=None, about='', register_date=datetime.utcnow):
        super().__init__()
        self._username = username
        self._passwd_hash = generate_password_hash(passwd)
        if not email:
            raise ValueError('Email can\'t be empty!')
        self._email = email
        self._friendly_name = friendly_name or username
        self._about = about
        self._register_date = register_date() if callable(register_date) else register_date
        self._following_count = 0
        self._followers_count = 0
        self._is_deleted = False
        self._last_seen = self._register_date
        self._posts_cnt = 0

    @staticmethod
    def __get_fuck(cond):
        return None
    __custom_query = {
        'get_fuck': __get_fuck
    }
    query = BaseQuery(app.mongodb.users, __custom_query)

    username = db_property('_username')
    email = db_property('_email')
    friendly_name = db_property('_friendly_name')
    about = db_property('_about')
    register_date = db_property('_register_date')
    following_count = db_property('_following_count')
    followers_count = db_property('_followers_count')
    last_seen = db_property('_last_seen')
    posts_cnt = db_property('_posts_cnt')
    passwd_hash = db_property('_passwd_hash')
    is_deleted = db_property('_is_deleted')

    def __repr__(self):
        return f"User(id={self._id},username={self._username},friendly_name={self._friendly_name},email={self._email})"

    def save(self):
        pass

    def check_password(self, password: str):
        return check_password_hash(self._passwd_hash, password)

    def avatar(self, size):
        digest = md5(self._email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

    def get_all_posts(self):
        pass

    def get_all_followers(self):
        pass

    def get_all_following(self):
        pass

    def unregister(self):
        pass

    def reset_password(self, passwd):
        pass
