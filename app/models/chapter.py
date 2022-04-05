# -*- coding: utf-8 -*-

from app import db
from .book import Book

class Chapter(db.Model):
    __tablename__ = 'chapters'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    title = db.Column(db.String(), nullable=True, default='')
    content = db.Column(db.String(), nullable=False)

    def __repr__(self):
        if self.title:
            return "<Chapter#{} [{}] />".format(self.id, self.title)
        return "<Chapter#{} />".format(self.id)
