# moneyviz

# Local development environment
Run these commands to install dependencies and start the site.

Install the Heroku CLI app and pipenv:
```
wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh
sudo apt-get update
sudo apt-get install heroku
sudo pip install pipenv
```

To install a postgres database and set up a user:
```
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres psql
CREATE DATABASE moneyviz;
CREATE USER moneyviz WITH PASSWORD '<some password>';
ALTER ROLE moneyviz SET client_encoding TO 'utf8';
ALTER ROLE moneyviz SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE moneyviz TO moneyviz;
\q (or CTRL+d)
```

Create a .env file in the project root:
```
export DATABASE_URL=postgres://moneyviz:password@localhost:5432/moneyviz
export DEBUG=True
```

Install the requirements and set up the database:
```
pipenv install
pipenv shell
python manage.py makemigrations
python manage.py migrate auth
python manage.py migrate
python manage.py createsuperuser
python manage.py backfill_api_keys
heroku local
```

# Transaction API
Documentation to follow. All requests are authenticated with API keys, using
the HTTP Authorization header, in the format `ApiKey <username>:<apikey>`.

The API key can be found on the User object: `user.api_key.key`

There is a Postman collection export in the root of the project which can be
used to make testing the API easier. Just install Postman, import this
collection using the JSON file, and set the Postman environment variables for
`url`, `user` and `apikey`.
