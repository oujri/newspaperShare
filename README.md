# Newspaper App

## Getting Started

Create your python3 virual environnemnet with
```
virtualenv env
```

### Prerequisites

* Create database journal in your PostgreSql server 
* Modify your **settings.py** DATABASES info
* migrate

```
python manage.py migrate
```

## Installing

Run this on Django shell to exclude contentype data

```
python3 manage.py shell
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()
```

Then copy the data provided in [datadump.json](https://github.com/oujri/newspaperShare/blob/share/datadump.json) into your database

```
python3 manage.py loaddata datadump.json
```

## Running

```
python manage.py runserver
```
