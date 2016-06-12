# moneyviz

Add valid Google OAuth key and secret to moneyviz/settings.py (the 
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY and SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET variables).
Alternatively, contact Karl to get a key for testing.

# Vagrant development environment
This method has the benefit of matching production most closely and should be 
the preferred way to test locally.

Just run 'vagrant up' in the root folder to use the Vagrantfile and provision a
development VM accessible from the host on localhost:8000. Use 'vagrant 
suspend' to keep the dev server running - there is currently no startup script,
just a provisioning script.

# Local development environment
Run these commands to install dependencies and start the site:
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
python manage.py backfill_api_keys
```

# Transaction API
Documentation to follow. All requests are authenticated with API keys, using
the HTTP Authorization header, in the format `ApiKey <username>:<apikey>`.

The API key can be found on the User object: `user.api_key.key`

There is a Postman collection export in the root of the project which can be
used to make testing the API easier. Just install Postman, import this
collection using the JSON file, and set the Postman environment variables for
`url`, `user` and `apikey`.
