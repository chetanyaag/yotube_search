FROM python:latest

WORKDIR /app


RUN pip install google-api-python-client pytube

COPY downloadvVdeo.py ./

CMD python downloadvVdeo.py