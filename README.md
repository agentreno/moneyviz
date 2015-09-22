# moneyviz

Add valid Google OAuth key and secret to moneyviz/settings.py (the 
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY and SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET variables).
Alternatively, contact Karl to get a key for testing.

Run these commands to install dependencies and start the site:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
