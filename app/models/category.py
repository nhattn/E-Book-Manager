# -*- coding: utf-8 -*-

from app import db
from .book import Book

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        if self.name:
            return "<Category#{} [{}] />".format(self.id, self.name)
        return "<Category#{} />".format(self.id)
