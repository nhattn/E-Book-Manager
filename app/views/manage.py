# -*- coding: utf-8 -*-

from app import engine, RANDOM_UID, db
from flask import render_template, abort, request, jsonify
from ..models.book import Book
from ..models.author import Author
from datetime import datetime
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

    query = Book.query.filter(Book.id != book.id).order_by(Book.created.desc()).paginate(1, 5, error_out=False)
    argv = {
        'site_title':book.name,
        'book' : book,
        'recents' : query.items
    }
    return render_template('ebook.html', **argv)

@engine.route('/newbook', methods=['POST'])
def newbook():
    if request.content_type and "application/json" in request.content_type:
        data = request.get_json()
    else:
        data = request.form
    name = data.get("name","").strip()
    if not name:
        return jsonify({
            "error":"Name is not valid"
        })
    book = Book.query.filter(Book.name == name).first()
    if bool(book):
        return jsonify({
            "error": "Book is exists"
        })
    author = data.get("author","").strip()
    if not author:
        return jsonify({
            "error":"Author is valid"
        })
    if author.isdigit():
        auth = Author.query.get(int(author))
        if not auth:
            return jsonify({
                "error":"Author is valid"
            })
    else:
        auth = Author.query.filter(Author.name == author).first()
        if auth:
            author = str(auth.id)
        else:
            auth = Author()
            auth.name = author
            db.session.add(auth)
            try:
                db.session.commit()
                author = str(auth.id)
            except:
                db.session.rollback()
                return jsonify({
                    "error":"Could not add book author"
                })

    book = Book()
    book.name = name
    book.source = data['source'].strip() if 'source' in data else ''
    book.isbn = data['isbn'].strip() if 'isbn' in data else ''
    book.cover = data['cover'].strip() if 'cover' in data else ''
    book.author_id = int(author)
    book.created = datetime.now()
    
    db.session.add(book)
    try:
        db.session.commit()
        return jsonify({
            "name":book.name,
            "source":book.source,
            "isbn":book.isbn,
            "author":book.author.name,
            "created":str(book.created)
        })
    except:
        db.session.rollback()
        return jsonify({
            "error":"Could not create book"
        })
