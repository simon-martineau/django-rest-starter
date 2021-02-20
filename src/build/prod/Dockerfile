#!/bin/sh

FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV APP_DIR=/home/app
ENV PATH="/home/app/.local/bin:${PATH}"

RUN useradd -ms /bin/bash app
WORKDIR $APP_DIR

COPY build/requirements.base.txt ./requirements/
COPY . ./
COPY build/prod/entrypoint.sh ./entrypoint.sh
RUN mkdir static
RUN mkdir media

RUN chown app:app -R $APP_DIR
USER app

RUN pip install --upgrade pip
RUN pip install -r requirements/requirements.base.txt
RUN pip install gunicorn==20.0.4

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/home/app/entrypoint.sh"]




