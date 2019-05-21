FROM ubuntu
#FROM mysql

RUN apt-get update

RUN apt-get -y install python3.7
RUN apt-get -y install python3-pip
RUN apt-get -y install vim
RUN apt-get -y install wget
RUN apt-get -y install busybox
RUN apt-get -y install chromium-chromedriver


COPY \ui_lib\ /usr/local/app/ui_lib/
COPY \utils\ /usr/local/app/utils/
COPY \main.py /usr/local/app/
COPY \requirements.txt /usr/local/app/
#COPY \chromedriver\ /usr/local/chromedriver/
COPY start.sh /start.sh

RUN mkdir -p /usr/bin/google-chrome/

RUN wget "https://chromedriver.storage.googleapis.com/2.46/chromedriver_linux64.zip"
RUN busybox unzip chromedriver_linux64.zip
RUN chmod a+x chromedriver
RUN mv chromedriver /usr/bin/


WORKDIR /usr/local/app

RUN pip3 install virtualenv
RUN pip3 install pyvirtualdisplay

RUN pip3 install -r /usr/local/app/requirements.txt

ENV PATH="/usr/local:${PATH}"
ENV PATH="/usr/bin/google-chrome/:${PATH}"
RUN chmod 777 /usr/bin/google-chrome/

CMD ["python3", "main.py"]
