from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: #Nested namespace for Configuration, keep Configurationin one place
        model = User #model that will be affected will be User model form.save() will sae in user model
        fields = ['username', 'email', 'password1', 'password2']

#create model form which allows us to create a form that wil work with spacific database model
#Now we want a form that will update our user model
class UserUpdateForm(forms.ModelForm): #allow us to update name and email
    email = forms.EmailField()

    class Meta: #Nested namespace for Configuration, keep Configurationin one place
        model = User #model that will be affected will be User model form.save() will sae in user model
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):#allow us to update profile pic
    class Meta:
        model = Profile
        fields = ['image']
