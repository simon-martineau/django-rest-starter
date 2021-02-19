#!/bin/sh

FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV APP_DIR=/home/app
ENV PATH="/home/app/.local/bin:${PATH}"


RUN useradd -ms /bin/bash app
USER app

RUN pip install --upgrade pip

WORKDIR $APP_DIR

COPY --chown=app:app build/requirements.base.txt ./requirements/
RUN pip install -r requirements/requirements.base.txt
RUN pip install gunicorn==20.0.4

COPY --chown=app:app . .
COPY --chown=app:app build/prod/entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/home/app/entrypoint.sh"]




