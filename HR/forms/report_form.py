from django import forms
from django.contrib.auth.models import User

class ReportForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())