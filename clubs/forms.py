from django import forms
from clubs.models import *

class UserForm(forms.ModelForm):

    password  = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class ClubForm(forms.Form):

    class Meta:
        model = Club
        fields = "__all__"

class ClubEventForm(forms.Form):

    class Meta:
        model = ClubEvent
        fields = "__all__"

class PhotoForm(forms.Form):

    class Meta:
        model = Photos
        fields = "__all__"

class PageAdminForm(forms.Form):

    class Meta:
        model = PageAdmin
        fields = "__all__"

class SecretaryForm(forms.Form):

    class Meta:
        model = Secretary
        fields = "__all__"

class JointSecretaryForm(forms.Form):

    class Meta:
        model = JointSecretary
        fields = "__all__"
