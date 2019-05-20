class BookItem(object):

    def __init__(self, book_name=None, book_author=None, book_date=None, book_reviews=None, book_rating=None, book_price=None, element=None):
        self.book_name = book_name
        self.book_author = book_author
        self.book_date = book_date
        self.reviews = book_reviews
        self.rating = book_rating
        self.price = book_price
        self.element = element

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
        return self.book_name[:199], self.book_author[:199], self.book_date[:29], self.reviews[:9], self.rating[:9], self.price[:9]
