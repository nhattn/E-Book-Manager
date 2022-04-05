# -*- coding: utf-8 -*-

def get_list_pages(page, pages):
    start = page - 2
    if start <= 0:
        start = 1

    end = start + 4
    if end > pages:
        end = pages

    if end - start < 4:
        start = end - 4
        if start <= 0:
            start = 1

    return {
        "start": start,
        "page": page,
        "end": end,
        "pages": pages
    }

def is_async(req):
    request_xhr_key = req.headers.get('X-Requested-With')
    if request_xhr_key and request_xhr_key.lower() == 'xmlhttprequest':
        return True
    return False
