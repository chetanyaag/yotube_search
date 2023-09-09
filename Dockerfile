FROM python:latest

WORKDIR /app


RUN pip install google-api-python-client pytube

COPY download.py ./

CMD python download.py