FROM python:3.6-alpine

RUN adduser -D wiebenik

WORKDIR /casus-groep7/

COPY requirements.txt requirements.txt
RUN python -m venv env
RUN env/bin/pip install -r requirements.txt

COPY . .
RUN chmod +x boot.sh

ENV FLASK_APP app.py

RUN chown -R wiebenik:wiebenik ./
USER wiebenik

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]