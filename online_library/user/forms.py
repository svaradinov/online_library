
from django import forms

from online_library.user.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
