from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Actor
from .models import Serials
from .forms import Form
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


class SerialsView(View):
    def get(self, request):
        serials = Serials.objects.all()
        return render(request, "serials/serials_list.html", {"serials": serials})


class SerialDetailView(View):
    def get(self, request):
        serials = Serials.objects.all()
        return render(request, "serials/single_serial.html", {"serials": serials})


class SingleSerial(View):
    def get(self, request, id):
        serial = get_object_or_404(Serials, id=id)
        return render(request, "serials/detail_serial.html", {"serial": serial})


class ActorView(View):
    def get(self, request, id):
        serial = get_object_or_404(Actor, id=id)
        return render(request, "serials/actor.html", {"serial": serial})


def add_list(request):
    context = {'list': Serials.objects.all()}
    return render(request, 'serials/mySerial.html', context)


def serials_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = Form()
        else:
            serials = Serials.objects.get(pk=id)
            form = Form(instance=serials)
        return render(request, 'serials/serials_form.html', {'form': form})
    else:
        if id == 0:
            form = Form(request.POST)
        else:
            serials = Serials.objects.get(pk=id)
            form = Form(request.POST, instance=serials)
        if form.is_valid():
            form.save()
        return redirect('/list/')


def delete_list(request, id):
    serials = Serials.objects.get(pk=id)
    serials.delete()
    return redirect('/list/')


@login_required
def Register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = name

        new_user.save()
        return redirect('login')

    return render(request, 'users/signUp.html', {})


def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('serials_list')
        else:
            return HttpResponse('Error, user does not exist')

    return render(request, 'users/login.html', {})


def logoutuser(request):
    logout(request)
    return redirect('login-page')
