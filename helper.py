def is_isbn_or_key(word):
    # 编写业务逻辑 判断是关键字还是isbn
    # isbn isbn13 13个0-9的数字
    # isbn 10个0到9的数字 包含 -
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key
