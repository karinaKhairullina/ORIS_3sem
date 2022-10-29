from django.http import HttpResponseRedirect
from .models import ToDoList


def create(request):
    if request.method == "POST":
        list = ToDoList()
        list.to_do = request.POST.get("Начать бегать по утрам")
        list.until_date = request.POST.get("2022-10-31")
        list.save()
    return HttpResponseRedirect("/")

