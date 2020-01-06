import json

from flask import jsonify, request, render_template, flash

from app.forms.book import SearchForm
from app.view_models.book import BookCollection
from app.web import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


@web.route('/book/search')
def search():
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q,page)
        # books.fill(yushu_book,q)
        return json.dumps(books, default=lambda  o:o.__dict__)
    else:
        return jsonify(form.errors)



@web.route('/test')
def test():
    r = {
        "name":"happy",
        'age' : 18
    }
    flash('hello qiyue',category='error')
    flash('hello jiuyue1',category='warning')
    return render_template('test.html',data=r)