FROM python:3.7.9-stretch

RUN pip install requests
RUN pip install datetime

ADD repolist.py /
ADD repolist.txt /

CMD [ "python", "./repolist.py" ]