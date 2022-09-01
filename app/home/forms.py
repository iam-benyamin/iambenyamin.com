from django import forms

from home.models.connect_me import ConnectMe as ConnectMeModel


class ConnectMeForm(forms.ModelForm):

    class Meta:
        model = ConnectMeModel
        fields = ["name", "email", "phone", "subject", "message"]