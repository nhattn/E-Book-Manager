# -*- coding: utf-8 -*-

from app import engine, RANDOM_UID

@engine.template_filter("isbn")
def the_isbn(id):
    return id + RANDOM_UID
