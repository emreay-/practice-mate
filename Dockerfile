FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get install apt-transport-https \ 
    && apt-get update -y \ 
    && apt-get install --no-install-recommends -y make gcc libpq-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip

COPY . /practice-mate
RUN pip3 install /practice-mate