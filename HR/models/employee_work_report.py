from HR.models.day import Day
from HR.models.employee import Employee
from HR.models.month import Month
from HR.models.year import Year
from enums.work_type import WorkType
from django.db import models
from django_currentuser.middleware import get_current_user

class EmployeeWorkReport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,default=0)   
    work_date_year = models.ForeignKey(Year, on_delete=models.CASCADE,default=1)
    work_date_month = models.ForeignKey(Month, on_delete=models.CASCADE,default=1)
    work_date_day =  models.ForeignKey(Day, on_delete=models.CASCADE,default=1)
    work_time = models.IntegerField()
    work_type =  models.CharField(choices=[(w.value, w.value) for w in WorkType],max_length=50)
    description = models.TextField()

    def save(self, *args, **kwargs):
        user_id = get_current_user().id
        self.employee = Employee.objects.get(user_id=user_id)
        return super(EmployeeWorkReport, self).save(*args, **kwargs)
        

