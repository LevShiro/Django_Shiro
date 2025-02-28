from django.contrib.auth import get_user_model
from django import forms
from django.forms import TextInput,PasswordInput,ImageField
from django.contrib.auth.forms import AuthenticationForm

User=get_user_model()

class EditProfileImageForm(forms.ModelForm):
    new_photo = forms.ImageField(required=False) #required = False убирает "Выберите файл"
    class Meta:
        model = User
        fields = ['photo']

class EditProfileNameForm(forms.ModelForm):
    new_username = forms.CharField(min_length=3,max_length=10,widget=TextInput(attrs={
        'class':'form-input',
        'placeholder':'Новое имя'
    }))
    password = forms.CharField(widget=PasswordInput(attrs={
        'class':'form-input',
        'placeholder':'Пароль'
    }))
    class Meta:
        model = User
        fields = ['password']
