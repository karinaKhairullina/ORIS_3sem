from django import forms
from .models import Salespeople

class Forms_Salespeople(forms.ModelForm):
    class Meta:
        model = Salespeople
        fields = ('name', 'city') #заголовки будут всплывать в html
