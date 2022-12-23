from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Actor
from .models import Serials
from .forms import Form


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
    context = {'list' : Serials.objects.all()}
    return render(request, 'serials/mySerial.html',context)


def serials_form(request):
    if request.method == "GET":
        form = Form()
        return render(request, 'serials/serials_form.html', {'form': form})
    else:
        form = Form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list/')

def delete_list(request):
    return


class Register(View):
    def get(self, request):
        serials = Serials.objects.all()
        return render(request, "serials/register.html", {"serials": serials})


class Reg(View):
    def get(self, request):
        serials = Serials.objects.all()
        return render(request, "serials/reg.html", {"serials": serials})




    



