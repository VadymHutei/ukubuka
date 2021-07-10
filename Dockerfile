FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV TZ Europe/Kiev

COPY ./app /app