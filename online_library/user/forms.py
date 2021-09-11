from django import forms

from online_library.user.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class DeleteUserForm(UserForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'
