import logging
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template.context import RequestContext

logger = logging.getLogger(__name__)

# Create your views here.
@login_required(login_url='/loginpage')
def index(request):
   return render(request, 'main/index.html')

def loginpage(request):
   context = RequestContext(request,
         {'request' : request, 'user' : request.user})
   return render_to_response('main/login.html',
         context_instance=context)

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
      return redirect('/loginpage')

@login_required(login_url='/loginpage')
def servePartial(request, partialname):
   context = RequestContext(request,
         {'request' : request, 'user' : request.user})
   return render_to_response('main/' + partialname + '.html',
         context_instance=context)


@login_required(login_url='/loginpage')
def doLogout(request):
   logout(request)
   return redirect('/loginpage')

@login_required(login_url = '/loginpage')
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
   
@login_required(login_url = '/loginpage')
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
