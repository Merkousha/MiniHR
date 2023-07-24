from django.shortcuts import get_object_or_404, redirect, render
from HR.forms.employee_work_report_form import EmployeeWorkReportForm
from HR.forms.report_form import ReportForm
from HR.models.employee import Employee
from .models.employee_work_report import EmployeeWorkReport

def home(request):
    return render(request, 'home.html')

def report(request):
    form = ReportForm()
    return render(request, 'report.html', {'form': form})

def report_results(request):
    employee = get_object_or_404(Employee, user_id=request.user.id)
    reports = EmployeeWorkReport.objects.filter(employee=employee).select_related('employee').all()
    return render(request, 'report_results.html', {'reports': reports})
