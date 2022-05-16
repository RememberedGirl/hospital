from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User, AbstractUser

from .models import *

#masha code patient
class PatientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sex'].empthy_label = "Пол не выбран"


    class Meta:
        model = Patient
        fields = ['name', 'date_birth', 'sex', 'citizenship', 'photo',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'citizenship': forms.TextInput(attrs={'class': 'form-control'}),
        }

    class AnamnesisForm(forms.ModelForm):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        class Meta:
            model = Game
            fields = ['room', 'time0', 'time1', 'day', 'doctor']

#end masha code patient
class AnamnesisForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Anamnesis
        fields = ['diagnosis', 'time0', 'time1', 'info1', 'info0', 'info2', 'doctor']

#end masha code anamnesis

class PlayerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].empthy_label = "Специальность позиция не выбрана"


    class Meta:
        model = Player
        fields = ['name', 'date_birth', 'role', 'citizenship', 'photo', 'biog', 'public_photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'citizenship': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GameForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Game
        fields = ['room', 'time0', 'time1', 'day', 'doctor']


class GamePlayerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Player_Game
        fields = ['player', 'game', 'count_washers', 'yellow_card', 'read_card']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин  ', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль  ', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Player
        fields = ['name', 'date_birth', 'role', 'citizenship', 'number', 'photo', 'biog', 'indicator', 'public_photo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_birth': forms.TextInput(attrs={'class': 'form-control'}),
            'citizenship': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
