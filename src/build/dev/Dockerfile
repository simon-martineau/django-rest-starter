FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code

COPY build/requirements.base.txt build/requirements.test.txt /code/requirements/
RUN pip install -r requirements/requirements.base.txt && \
		pip install -r requirements/requirements.test.txt

COPY build/dev/start_dev.sh /
COPY . /code/