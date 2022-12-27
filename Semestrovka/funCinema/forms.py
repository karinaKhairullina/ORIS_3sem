from django import forms
from .models import Serials
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
=======

>>>>>>> e7ded3b67c590bafff423e92a137fc3d214f3c49

class Form(forms.ModelForm):
    class Meta:
        model = Serials
<<<<<<< HEAD
        fields = ('title', 'link')
        labels = {
            'title': 'Название',
=======
        fields = ('title', 'genre', 'link')
        labels = {
            'title': 'Название',
            'genre': 'Жанр',
>>>>>>> e7ded3b67c590bafff423e92a137fc3d214f3c49
            'link': 'Ссылка'
        }

    def __int__(self, *args, **kwargs):
<<<<<<< HEAD
        super(Form, self).__init__(*args, **kwargs)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
=======
        super(Form, self).__init__(*args, **kwargs)
>>>>>>> e7ded3b67c590bafff423e92a137fc3d214f3c49
