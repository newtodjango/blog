import imp
from socket import fromshare
#from xml.etree.ElementTree import Comment
from django import forms

from .models import comment

class commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name','email','body']

