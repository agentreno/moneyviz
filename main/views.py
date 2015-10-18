import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template.context import RequestContext

logger = logging.getLogger(__name__)

# Create your views here.
@login_required
def index(request):
   return render(request, 'main/index.html')

def loginpage(request):
    return render(request,'main/login.html',
        {'request' : request, 'user' : request.user}
    )

def doLogin(request):
   if not request.method == 'POST' or \
      not request.POST.__contains__('username') or \
      not request.POST.__contains__('password') or \
      request.POST['username'] == "" or \
      request.POST['password'] == "":
         return redirect('/loginpage')

   username = request.POST['username']
   password = request.POST['password']
   user = authenticate(username=username, password=password)
   if user is not None:
      logger.info("Successful login: " + user.username)
      login(request, user)
      return redirect('/')
   else:
      logger.info("Failed login")
      return render(request, 'main/login.html',
        {'login_error': True}
      )

@login_required
def servePartial(request, partialname):
    return render(request, 'main/' + partialname + '.html',
        {'request' : request, 'user' : request.user}
    )

@login_required
def doLogout(request):
   logout(request)
   return redirect('/loginpage')

@login_required
def updateUserInfo(request):
   if request.method == "POST" and \
   "first_name" in request.POST and \
   "last_name" in request.POST and \
   "email" in request.POST:
      first_name = request.POST["first_name"]
      last_name = request.POST["last_name"]
      email = request.POST["email"]
      user = request.user
      user.first_name = first_name.strip()
      user.last_name = last_name.strip()
      user.email = email
      user.save()
   return redirect('/')

@login_required
def updateUserPassword(request):
   if request.method == "POST" and \
   "current_password" in request.POST and \
   "new_password" in request.POST and \
   "new_password_confirm" in request.POST:
      current_password = request.POST['current_password']
      new_password = request.POST['new_password']
      new_password_confirm = request.POST['new_password_confirm']
      user = request.user
      if user.check_password(current_password) and new_password == new_password_confirm:
         user.set_password(new_password)
         user.save()
         user_auth = authenticate(username=user.username, password=new_password)
         login(request, user_auth)
   return redirect('/')
