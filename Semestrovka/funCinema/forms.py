from django import forms
from .models import Serials


class Form(forms.ModelForm):
    class Meta:
        model = Serials
        fields = ('title', 'link')
        labels = {
            'title': 'Название',
            'link': 'Ссылка'
        }

    def __int__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)