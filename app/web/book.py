from flask import make_response, jsonify, request
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web

# blueprint


@web.route('/book/search')
def search():
    """
        q : 代表普通关键字 或者 isbn
        page
        ?q=金庸&page=1
    :return:
    """
    q = request.args['q']
    page = request.args['page']
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
        # dict 序列化 -> 将results转为json
    # This is an API
    return jsonify(result)
    # return json.dump(result), 200, {'content-type': 'application/json'}


# 定义视图函数
# 通过http请求来访问该函数
# 确保唯一URL原则
@web.route('/hello')  # 装饰器 定义路由 传入URL路径
def hello_world():  # 视图函数 类似于控制器 controller
    # 基于类的视图(即插视图)
    headers = {
        'content-type': 'text/plain',
    }
    response = make_response('<html></html>', 200)
    response.headers = headers
    return response  # 视图函数的return Flask做了封装 还会返回status code
    # 返回content type -> 默认值 text/html
