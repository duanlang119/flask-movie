from app.libs.http_util import HTTP
from flask import current_app

class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&start={}&count={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self,isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def __fill_single(self,data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_conllection(self,data):
        self.total = data['total']
        self.books = data['books']

    def search_by_keyword(self, keyword,page=1):
        url = self.keyword_url.format(keyword,current_app.config['PER_PAGE'],self.calculate_start(page))
        print(url)
        result = HTTP.get(url)
        # dict
        self.__fill_conllection(result)

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']