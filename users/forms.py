from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

#create your forms here

class CustomUserCreationForm(UserCreationForm):
    '''
    class for user creation form
    '''
    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    '''
    class for user change form
    '''
    class Meta:
        model = CustomUser
        fields = ("email",)