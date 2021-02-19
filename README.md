# django-rest-starter

##### A starter template for building rest apis with django
Replace every instance of "django-rest-starter" in the code by the name of your app and you're good to go!

Make sur to look at the [pycharm config](ideaConfig.md)

## Installation
### Requirements
You will need the following to run the app
- docker ([installation](https://docs.docker.com/get-docker/))
- docker-compose ([installation](https://docs.docker.com/compose/install/))

### Setup
Perform these steps to quickly get started

**Note:** ports 8000 and 5444 need to be available
```bash
cd someapi
docker-compose -f ./docker-compose.dev.yml up -d
```

The api should be available at http://localhost:8000

You can always use the following command to stop execution:
```bash
docker-compose -f ./docker-compose.dev.yml down
```

### Tests
Use this command to run tests:
```bash
docker-compose -f docker-compose.dev.yml run api sh -c "python manage.py test"
```