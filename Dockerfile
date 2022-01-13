FROM afzalsaiyed/corecare_base:latest
ENV PYTHONUNBUFFERED 1
WORKDIR /cartdrop
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY /requirements/base.txt .
COPY /requirements/testing.txt .
RUN pip install -r testing.txt