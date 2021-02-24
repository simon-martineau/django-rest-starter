# Deploy notes
## Environement variables
The following environment varialbes need to be set on the dokku/heroku app environment:
```dotenv
DJANGO_SECRET_KEY  # Your django secret key for production
DJANGO_SETTINGS_MODULE  # {{cookiecutter.project_slug}}.settings.production

# These apply to the default user created by the postdeploy script
# If the user already exists, the creation is skipped
DJANGO_SUPERUSER_EMAIL 
DJANGO_SUPERUSER_PASSWORD

# Aws S3 credentials
AWS_ACCESS_KEY_ID  
AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME

# These IP addresses will not receive a 404 while visiting any url that begins with /admin
DJANGO_ADMIN_WHITELIST_IPS
```
{% set project_with_hyphens = cookiecutter.project_slug | replace("_", "-") %}
## Dokku
Here are the steps to deploy using dokku

See https://dokku.com/docs/getting-started/installation/ for installing dokku
#### On the dokku host
These commands need to be executed on the dokku host
```shell script
sudo dokku apps:create {{project_with_hyphens}}
sudo dokku plugins:install https://github.com/dokku/dokku-postgres.git postgres
sudo dokku postgres:create drs-database
sudo dokku postgres:link drs-database {{project_with_hyphens}}
```

Don't forget to set the environment variables for your app using:
```shell script
dokku config:set {{project_with_hyphens}} KEY1=value1 KEY2=value2
```

Also, set your domains for the app like this: (and don't forget to point your dns records to the dokku host,
at least for the active apps)
```shell script
dokku domains:add {{project_with_hyphens}} {{cookiecutter.domain}}
```

#### On the git repo
All we need is to add the remote and push a subtree:
```shell script
git remote add dokku dokku@<server_ip>:{{project_with_hyphens}}
git subtree push --prefix src dokku master
```

#### SSL with letsencrypt
Once your app is up and running, you need to enable https with the following
```shell script
sudo dokku plugin:install https://github.com/dokku/dokku-letsencrypt.git
sudo dokku config:set --no-restart {{project_with_hyphens}} DOKKU_LETSENCRYPT_EMAIL=your@email.tld
sudo dokku letsencrypt {{project_with_hyphens}}
```

And you're done!