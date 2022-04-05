# -*- coding: utf-8 -*-

from app import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    cover = db.Column(db.String, nullable=True)
    source = db.Column(db.String, nullable=True)
    isbn = db.Column(db.String, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=True, default=0)
    created = db.Column(db.DateTime, nullable=False, default=datetime(1970, 1, 1))
    published = db.Column(db.DateTime, nullable=True, default=datetime(1970, 1, 1))
    modified = db.Column(db.DateTime, nullable=True, default=datetime(1970, 1, 1))

    def __repr__(self):
        if self.name:
            return "<Book#{} [{}] />".format(self.id, self.name)
        return "<Book#{} />".format(self.id)
