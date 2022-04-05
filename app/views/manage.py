# -*- coding: utf-8 -*-

from app import engine, RANDOM_UID
from flask import render_template, abort

@engine.route('/')
def manage():
    return render_template('index.html')

@engine.route('/ebook/<int:id>')
def ebook(id=0):
    id_ = id - RANDOM_UID
    if id_ <= 0:
        abort(404)
    return render_template('ebook.html', site_title="Detail")
