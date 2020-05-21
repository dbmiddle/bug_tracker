from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from tracker.models import MyUser
from tracker.forms import LoginForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def loginview(request):
    html = 'login_form.html'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                    )

    form = LoginForm()

    return render(request, html, {'form': form})


def logoutview(request):
    if request.method == 'GET':
        logout(request)

    return HttpResponseRedirect(reverse('login'))