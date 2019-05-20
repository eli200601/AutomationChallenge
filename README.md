# AutomationChallenge
Automation Challenge with docker
---------------------------------

This application use Selenium to access amazon.com
the script take the first 4 result items.
and save it into a MySQL database


To run script from windows:
run the following commands:
  * clone the git repository
  * $ pip install -r requirements.txt
  * $ python main.py
  
- Precondition: You need MySQL server installed and running with user root:root
- DB must have 'book_list' database
- 'book_list' database must have 'books' table

----------------------------------------------------------------------------------
to run via container:
  * clone the git repository
  * $ docker build -t automation_challenge .
  * $ docker run -i -t --entrypoint bash automation_challenge
