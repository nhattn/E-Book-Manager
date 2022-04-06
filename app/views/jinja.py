# -*- coding: utf-8 -*-

from app import engine, RANDOM_UID
import markdown
from flask import Markup
from .figure import FigureCaption

@engine.template_filter("isbn")
def the_isbn(id):
    return id + RANDOM_UID

@engine.template_filter('markdown')
def neomarkdown(markdown_content):
    return Markup(markdown.markdown(markdown_content, extensions=['tables','codehilite','fenced_code',FigureCaption()]))

@engine.template_filter('editor')
def contenteditor(markdown_content):
    content = markdown.markdown(markdown_content, extensions=['tables','codehilite','fenced_code',FigureCaption()])
    content = content.replace("<p>","<p spellcheck=\"false\" contenteditable=\"false\"><span class=\"editor\"></span>")
    content = content.replace("<h1>","<h1 spellcheck=\"false\" contenteditable=\"false\"><span class=\"editor\"></span>")
    content = content.replace("<h2>","<h2 spellcheck=\"false\" contenteditable=\"false\"><span class=\"editor\"></span>")
    content = content.replace("<h3>","<h3 spellcheck=\"false\" contenteditable=\"false\"><span class=\"editor\"></span>")
    content = content.replace("<h4>","<h4 spellcheck=\"false\" contenteditable=\"false\"><span class=\"editor\"></span>")
    content = content.replace("<h5>","<h5 spellcheck=\"false\" contenteditable=\"false\"><span class=\"editor\"></span>")
    content = content.replace("<h6>","<h6 spellcheck=\"false\" contenteditable=\"false\"><span class=\"editor\"></span>")
    content = content.replace("<figure>","<figure spellcheck=\"false\" contenteditable=\"false\"><span class=\"editor\"></span>")
    return Markup(content)
