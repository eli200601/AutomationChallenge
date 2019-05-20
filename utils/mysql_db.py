import pymysql


def _get_connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='book_list',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def insert_books_list_to_db(book_list):
    connection = _get_connection()
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `books` (`book_name`, `book_author`, `book_date`,`reviews`,`rating`,`price`)" \
                  " VALUES (%s, %s, %s, %s, %s, %s)"
            for book in book_list:
                print('insert')
                cursor.execute(sql, book.get_as_list())
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `books`"
            cursor.execute(sql,)
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()
