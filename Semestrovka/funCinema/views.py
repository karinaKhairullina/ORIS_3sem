from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from .models import Actor
from .models import Serials


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


class AddView(CreateView):
    model = Serials
    template_name = 'serials/add.html'
    fields = ['title', 'description', 'date', 'country', 'actors']


class Register(View):
    def get(self, request):
        serials = Serials.objects.all()
        return render(request, "serials/register.html", {"serials": serials})


class Reg(View):
    def get(self, request):
        serials = Serials.objects.all()
        return render(request, "serials/reg.html", {"serials": serials})




    



