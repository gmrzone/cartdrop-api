FROM python:3.9.6-slim-buster
RUN apt-get update && apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info -y
ENV PYTHONUNBUFFERED 1
WORKDIR /cartdrop
COPY /requirements/base.txt .
COPY /requirements/testing.txt .
RUN pip install -r testing.txt