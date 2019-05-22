# AutomationChallenge
Automation Challenge with docker
---------------------------------

This application use Selenium to access amazon.com.
the script take the first 4 result screen items.
and save it into a MySQL database


run script from windows CMD, from the repository folder:
* $ docker-compose up (wait until its up)
* $ python main.py

  
** Preconditions:
* you must have chromedriver.exe define in PATH
* $ pip install -r requirements.txt
* You must config in docker > settings > Shared Drives - the drive you running from, 
  Than reset docker service
s
