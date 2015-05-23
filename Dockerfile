FROM google/python
MAINTAINER Vincent Tertre <vincent.tertre@gmail.com>

RUN apt-get install -y libpq-dev git

WORKDIR /app

RUN virtualenv /env
ADD requirements.txt /app/requirements.txt
RUN /env/bin/pip install -r requirements.txt

ADD . /app

EXPOSE 8080
ENV PORT 8080

CMD ["/env/bin/gunicorn", "xdcc_subtitles.wsgi"]