from django import forms
from django.utils.translation import ugettext_lazy as _

class loginForm(forms.Form):
    username = forms.CharField(label=_("email"),
                               widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    passwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                       label=_("password"))

class basicForm(forms.Form):
    username = forms.CharField(label=_("username"),
                               widget=forms.TextInput(attrs={'placeholder': ''}))
    passwd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ''}),
                       label=_("password"))
    sid = forms.CharField(label=_("SID"),
                               widget=forms.TextInput(attrs={'placeholder': ''}))
    host = forms.CharField(label=_("host"),
                               widget=forms.TextInput(attrs={'placeholder': 'Hostname or IP'}))
    port = forms.CharField(label=_("port"),
                               widget=forms.TextInput(attrs={'placeholder': ''}))
