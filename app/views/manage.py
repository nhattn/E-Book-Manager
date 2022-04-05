# -*- coding: utf-8 -*-

from app import engine, RANDOM_UID
from flask import render_template, abort, request, jsonify
from ..models.book import Book
from ..models.author import Author
from .util import get_list_pages, is_async

@engine.route('/')
@engine.route('/page/<int:page>')
def manage(page=1):
    if page <= 0:
        page = 1
    limit = 10
    query = Book.query.order_by(Book.created.desc()).paginate(page, limit, error_out=False)
    argv = {
        "books": query.items,
        "navi":None
    }
    if query.pages > 1:
        argv['navi'] = get_list_pages(query.page, query.pages)
    if is_async(request):
        return jsonify(argv)

    return render_template('index.html', **argv)

@engine.route('/ebook/<int:id>')
def ebook(id=0):
    id_ = id - RANDOM_UID
    if id_ <= 0:
        abort(404)

    book = Book.query.get(id_)
    if not book:
        abort(404)

    query = Book.query.order_by(Book.created.desc()).paginate(1, 5, error_out=False)
    argv = {
        'site_title':book.name,
        'book' : book,
        'recents' : query.items
    }
    return render_template('ebook.html', **argv)
