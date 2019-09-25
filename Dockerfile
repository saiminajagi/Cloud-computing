FROM python:3.6

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

EXPOSE 8000
COPY init.sh /usr/local/bin/

RUN chmod u+x /usr/local/bin/init.sh
ENTRYPOINT ["init.sh"]
