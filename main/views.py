import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

logger = logging.getLogger(__name__)

# Create your views here.
@login_required(login_url='/login')
def index(request):
   return render(request, 'main/index.html')

def loginpage(request):
   return render(request, 'main/login.html')

def doLogin(request):
   if not request.method == 'POST' or \
      not request.POST.__contains__('username') or \
      not request.POST.__contains__('password') or \
      request.POST['username'] == "" or \
      request.POST['password'] == "":
         return redirect('/login')
   
   username = request.POST['username']
   password = request.POST['password']
   user = authenticate(username=username, password=password)
   if user is not None:
      logger.info("Successful login: " + user.username)
      login(request, user)
      return redirect('/')
   else:
      logger.info("Failed login")
      return redirect('/login')

@login_required(login_url='/login')
def servePartial(request, partialname):
   return render(request, 'main/' + partialname + '.html')


@login_required(login_url='/login')
def doLogout(request):
   logout(request)
   return redirect('/login')
