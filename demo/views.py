from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreatePersonalForm
from django.contrib.auth.decorators import login_required
from .models import personal

# Create your views here.

def base_view(request):
      return render(request, 'base.html')

@login_required(login_url='login_view')
def home(request):
      return render(request, 'index.html')


def page_profile(request):
      return render(request, 'profile.html')


def login_view(request):
      if  request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                  login(request, user)
                  return redirect('home')
      context = {}
      return render(request, 'signin.html', context)


def register(request):
      form = CreatePersonalForm()
      if request.method == 'POST':
            form = CreatePersonalForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect('login_view')
      context = {'form': form}
      return render(request, 'signup.html', context)