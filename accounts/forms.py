

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm
from .models import User

#Overriding base auth form to add custom error message
class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['invalid_login'] = 'Password incorrect, please try again.'
        
#Overriding the base creation form to take in an email instead of username
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        #Overriding the default User model w/ the one we created
        model = User
        
        #Adding first name and last name fields to the signup page
        fields = ('email','first_name', 'last_name')

class UserSettingsForm(ModelForm):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',]



