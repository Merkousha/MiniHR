from django import forms
from django.contrib import admin
from HR.forms.employee_work_report_form import EmployeeWorkReportForm
from HR.models import EmployeeWorkReport, Year, Month, WeekDay, Day, Employee, EmployeeType, Day, Gender


class MonthInline(admin.TabularInline):
    model = Month
    extra = 12
class YearModelAdmin(admin.ModelAdmin):
    inlines = [MonthInline]


class DayInline(admin.TabularInline):
    model = Day
    def get_extra(self, request, obj=None, **kwargs):
        # Set extra to 0 for edit page, 31 for create page
        if obj is None:
            return 31  # Number of inline forms to display in create page
        else:
            return 0  # Hide the extra empty form in edit page

class MonthModelAdmin(admin.ModelAdmin):
    inlines = [DayInline]

class EmployeeWorkReportAdmin(admin.ModelAdmin):
    form = EmployeeWorkReportForm


admin.site.register(Year, YearModelAdmin)
admin.site.register(Month, MonthModelAdmin)
admin.site.register(WeekDay)
admin.site.register(Day)

admin.site.register(Gender)
admin.site.register(EmployeeType)
admin.site.register(Employee)
admin.site.register(EmployeeWorkReport, EmployeeWorkReportAdmin)

