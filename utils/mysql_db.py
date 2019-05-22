import pymysql


def _get_connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='password',
                                 db='book_list',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def insert_books_list_to_db(book_list):
    connection = _get_connection()
    i = 0
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `books` (`book_name`, `book_author`, `book_date`,`reviews`,`rating`,`price`, `href`)" \
                  " VALUES (%s, %s, %s, %s, %s, %s, %s)"
            for book in book_list:
                cursor.execute(sql, book.get_as_list())
                i += 1
        connection.commit()
        print('Inserted {} items to DB'.format(str(i)))
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `books`"
            cursor.execute(sql,)
            result = cursor.fetchall()
            print('SELECT * FROM books:')
            print(result)
    finally:
        connection.close()
