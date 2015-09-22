from social.backends.google import GoogleOAuth2
from main.models import GoogleInfo

def save_avatar_url(backend, user, response, details, is_new=False,
      *args, **kwargs):
   if isinstance(backend, GoogleOAuth2):
      if response.get('image') and response['image'].get('url'):
         url = response['image']['url']
         if url != "":
            try:
               ginfo = user.googleinfo
               ginfo.avatar_url = url
               ginfo.save()
            except GoogleInfo.DoesNotExist:
               ginfo = GoogleInfo(user=user, avatar_url=url)
               ginfo.save()
