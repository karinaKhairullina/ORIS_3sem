from django.shortcuts import render, redirect
from main.models import Salespeople, Customers
from .forms import Forms_Salespeople

def input_Salespeople(request):
    form = Forms_Salespeople()
    if request.method == 'POST': #когда кнопку нажимаешь там вот эта штука делается
        form = Forms_Salespeople(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_Salespeople')
    return render(request, 'main.html', context= {'form': form})

def get_Salespeople(request):
    salespeople = Salespeople.objects.all()
    return render(request, 'main2.html', context={'salespeople': salespeople})




