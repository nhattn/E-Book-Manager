# -*- coding: utf-8 -*-

from app import db
from ..models.author import Author
from ..models.book import Book
from ..models.chapter import Chapter
from ..models.category import Category

def initdb():
    print("Initialized default DB")
    db.drop_all()
    db.create_all()
