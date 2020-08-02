

from django.contrib.auth.forms import AuthenticationForm

#Overriding base auth form to add custom error message
class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['invalid_login'] = 'Password incorrect, please try again.'
        
