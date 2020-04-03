## How to deploy

```
export dbUser=xyz
export dbPassword=xyz123
export AWS_PROFILE=whatever
export domainName=example.com
export certificateArn="arn:..."
export hostedZoneId="..."

npx serverless create_domain
./manage.py collectstatic
npx serverless deploy
npx serverless client deploy
sls wsgi manage --command "migrate"
sls wsgi manage --command "createsuperuser --username somebody --noinput --email somebody@example.com"
sls wsgi exec --command "from django.contrib.auth.models import User; u=User.objects.get(username='somebody'); u.set_password('letmein123'); u.save()"
sls wsgi manage --command "loaddata cups/data/cabinet.json"
```

## About Django

### Ecosystem

* heroku
* https://djangopackages.org
* serverless-wsgi
* django-rest-framework has its own ecosystem

### Conventions

* database agnostic (be careful - test against real database)
* structure. can "read" a django codebase e.g. settings.py, urls.py
* testing - transactions

### Libraries

* auth
* admin site
* i18n
* l10n
* geo

### Other

* kinda supposed to have a server
