# django-rest-starter
[![Build Status](https://travis-ci.com/simon-martineau/django-rest-starter.svg?branch=main)](https://travis-ci.com/simon-martineau/django-rest-starter)
[![codecov](https://codecov.io/gh/simon-martineau/django-rest-starter/branch/main/graph/badge.svg?token=MGCXZA5MRM)](https://codecov.io/gh/simon-martineau/django-rest-starter)
##### A starter template for building rest apis with django
Replace every instance of "django-rest-starter" in the code by the name of your app and you're good to go!

Make sure to look at the [pycharm config](ideaConfig.md)

## Development
### Requirements
You will need the following to run the app
- docker ([installation](https://docs.docker.com/get-docker/))
- docker-compose ([installation](https://docs.docker.com/compose/install/))

### Setup
Perform these steps to quickly get started

**Note:** ports 8000 and 5444 need to be available
```bash
cd someapi
docker-compose up -d
```

The api should be available at http://localhost:8000

You can always use the following command to stop execution:
```bash
docker-compose down
```

### Tests
Use this command to run tests:
```bash
docker-compose run api sh -c "python manage.py test"
```