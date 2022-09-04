from distutils import errors
import imp
from importlib.metadata import requires
from xml.dom import UserDataHandler
from django.contrib import messages
from multiprocessing import context
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth import get_user_model
from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/courses')

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data.get('username')
            messages.success(
                request, 'Succesfully created account for ' + name)
            login(request, user)
            return redirect('/courses')

        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = CreateUserForm()

    return render(
        request=request,
        template_name="register.html",
        context={"form": form}
    )


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('courses')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('courses')
            else:
                messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def osPage(request):
    if request.user.is_authenticated:
        return redirect('courses')
    else:
        # selected_os = print(request.POST['os'])
        context = {}
    return render(request, 'os.html')


@login_required(login_url='login')
def coursesPage(request):
    context = {}
    return render(request, 'courses.html')


@login_required(login_url='login')
def forumPage(request):
    context = {}
    return render(request, 'forum.html')


@login_required(login_url='login')
def quizzPage(request):
    context = {}
    return render(request, 'quizz.html')
