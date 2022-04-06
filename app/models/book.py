# -*- coding: utf-8 -*-

from app import db
from datetime import datetime

book_cats = db.Table(
    "book_cats",
    db.Column("book_id", db.Integer, db.ForeignKey("books.id")),
    db.Column("cat_id", db.ForeignKey("categories.id"))
)

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
    categories = db.relationship("Category", secondary=book_cats, backref=db.backref("book_cats", lazy="select"))

    def __repr__(self):
        if self.name:
            return "<Book#{} [{}] />".format(self.id, self.name)
        return "<Book#{} />".format(self.id)
