CREATE TABLE IF NOT EXISTS books(
book_id INT AUTO_INCREMENT,
book_name varchar(200),
book_author  varchar(200),
book_date varchar(30),
reviews  varchar(10),
rating  varchar(10),
price   varchar(10),
PRIMARY KEY (book_id)
)ENGINE=INNODB;