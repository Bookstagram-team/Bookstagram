from django.forms import ModelForm
from main.models import Item
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from .models import User
from book.models import Book

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

#untuk user

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_employee', 'is_customer')