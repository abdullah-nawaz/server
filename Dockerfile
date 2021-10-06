FROM python:3.6

ADD . /server
WORKDIR /server

# Install pre-requisites
RUN apt-get update
RUN apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    python3-dev

# Set the C_FORCE_ROOT environment variable for the Celery process, replace later
ENV C_FORCE_ROOT true

RUN pip3 install --upgrade pip
RUN pip3 install -r /server/requirements.txt
