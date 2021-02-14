## SirinSoftware

This application implement Alias app.

In my realisation I use Django managers for implementing custom methods. 
Also, I use django signals for implementing `pre_save` validation for new alias objects. 

As DB I use PostgreSQL, because it can store datetime object with microseconds precision, despite no-sql db as MongoDB, store date time field only in milliseconds precision 

# HOW TO START?
I use Manjaro Linux.
To start project you need python 3, postgresql. 

1. Clone git repo 
2. Install postgresql
3. Set environment variables or make bash file:
```
export SECRET_KEY='some_dev_key'
export DEBUG='1'
export DB_NAME='your_db_name'
export DB_USER='user'
export DB_PASS='password'

or

#!/bin/bash

export SECRET_KEY='some_dev_key'
export DEBUG='1'
export DB_NAME='your_db_name'
export DB_USER='user'
export DB_PASS='password'

#end bash file

source <bash_file_name>
```
4. Set up virtual env  `python -m venv venv`
5. Activate venv `source venv/bin/activate`
6. Install packages `pip install -r requirements.txt`
7. If you want to populate db  use `python manage.py populate_db`
8. If you want to test app use `python manage.py test`
9. If you what to test functionality use `python manage.py shell`
Some example of django shell session:
```
>>> from alias.models import Alias
>>> from datetime import datetime
>>> import pytz
>>> start = pytz.utc.localize(datetime.strptime('2020-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f"))
>>> end = pytz.utc.localize(datetime.strptime('2021-05-01 05:23:47.657264', "%Y-%m-%d %H:%M:%S.%f"))
>>> alias = 'alias1'
>>> target = 'target1'
>>> Alias.objects.create(alias=alias, target=target, start=start, end=end)
>>> Alias.objects.get_aliases(target=target, _from=start, to=end)
<QuerySet [<Alias: Alias object ()>]]>
>>> Alias.objects.alias_replace(existing_alias=alias, replace_at=end, new_alias_value='new_alias')
1
```
# HOW TO START WITH DOCKER?

1. Clone git repo 

2. Install docker [tutorial](https://docs.docker.com/engine/install/ubuntu/)
3. `sudo docker-compose build`
4. `sudo docker-compose up`

If you want to restart app just enter commands below:

```
sudo docker-compose down
sudo docker-compose up
```

#HOW TO TEST WITH DOCKER?

1. Clone git repo 

2. Install docker [tutorial](https://docs.docker.com/engine/install/ubuntu/)
3. `sudo docker-compose build`
4. `sudo docker-compose run app sh -c "python manage.py test"`

If you want to test some functionality, follow command below:

1. `sudo docker-compose run app sh -c "python manage.py shell"`

In the end of session user command below:

1. `sudo docker-compose down`