FROM afzalsaiyed/corecare_base:latest
ENV PYTHONUNBUFFERED 1
WORKDIR /cartdrop
COPY /requirements/base.txt .
COPY /requirements/testing.txt .
RUN pip install -r testing.txt