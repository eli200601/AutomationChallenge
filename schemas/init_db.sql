CREATE database if not exists book_list;

USE book_list;

DROP TABLE IF EXISTS books;

CREATE TABLE IF NOT EXISTS books(
book_id INT AUTO_INCREMENT,
book_name varchar(300),
book_author  varchar(300),
book_date varchar(30),
reviews  varchar(50),
rating  varchar(30),
price   varchar(10),
href   varchar(300),
PRIMARY KEY (book_id)
);