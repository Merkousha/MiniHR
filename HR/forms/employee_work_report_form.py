from django import forms

from HR.models.employee import Employee
from ..models import EmployeeWorkReport
from enums.work_type import WorkType
from django.contrib.auth import get_user_model
from django_currentuser.middleware import get_current_user

class EmployeeWorkReportForm(forms.ModelForm):
    class Meta:
        model = EmployeeWorkReport
        exclude = ['employee']