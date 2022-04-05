# -*- coding: utf-8 -*-

from app import db
from .book import Book

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    books = db.relationship("Book", backref=db.backref("author"), lazy=True)

    def __repr__(self):
        if self.name:
            return "<Author#{} [{}] />".format(self.id, self.name)
        return "<Author#{} />".format(self.id)
