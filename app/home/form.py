from django import forms

from home.models.connect_me import ConnectMe as ConnectMeModel


# TODO clean data
# TODO error handling
class ConnectMeForm(forms.ModelForm):

    class Meta:
        model = ConnectMeModel
        fields = ["name", "email", "phone", "subject", "message"]