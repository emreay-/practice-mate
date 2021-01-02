FROM ubuntu:18.04

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y

RUN apt-get install -y gcc git curl make zlib1g zlib1g-dev bzip2 libbz2-dev libreadline-dev libpq-dev sqlite sqlite3 openssl libssl-dev build-essential python3-pip

RUN pip3 install --upgrade pip

RUN curl https://pyenv.run | bash
ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 3.8.6
RUN pyenv virtualenv 3.8.6 base
RUN pyenv rehash

COPY . /practice-mate
RUN pip3 install /practice-mate
