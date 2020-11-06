FROM python:3.6-alpine

RUN adduser -D wiebenik

WORKDIR /casus-groep7/

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY server server

ENV FLASK_APP server/app.py

RUN chown -R wiebenik:wiebenik ./
USER wiebenik

EXPOSE 5000
