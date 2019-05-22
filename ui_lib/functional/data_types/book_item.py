class BookItem(object):

    def __init__(self, book_name=None, book_author=None, book_date=None, book_reviews=None, book_rating=None, book_price=None, element=None, is_book=False, href=None):
        self.book_name = book_name
        self.book_author = book_author
        self.book_date = book_date
        self.reviews = book_reviews
        self.rating = book_rating
        self.price = book_price
        self.element = element
        self.is_book = is_book
        self.href = href

    def __repr__(self):
        return "\tBook item:\n" \
               "\t\t\tBook Name: {name}\n" \
               "\t\t\tBook Author: {author}\n" \
               "\t\t\tDate: {date}\n" \
               "\t\t\tReview`s: {reviews}\n" \
               "\t\t\tRating: {rating}\n" \
               "\t\t\tPrice: {price}\n".format(name=self.book_name,
                                               author=self.book_author,
                                               date=self.book_date,
                                               reviews=self.reviews,
                                               rating=self.rating,
                                               price=self.price)

    def get_as_list(self):
        return self.book_name[:299], self.book_author[:299], self.book_date[:29], self.reviews[:29], self.rating[:29], self.price[:9], self.href[:299]
