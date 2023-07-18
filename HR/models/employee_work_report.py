from enums.work_type import WorkType
from django.db import models

class EmployeeWorkReport(models.Model):
    work_date = models.DateField()
    work_time = models.IntegerField()
    work_type =  models.CharField(choices=[(w.value, w.value) for w in WorkType],max_length=50)
    description = models.TextField()