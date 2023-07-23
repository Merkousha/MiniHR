from HR.models.day import Day
from HR.models.month import Month
from HR.models.year import Year
from enums.work_type import WorkType
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class EmployeeWorkReport(models.Model):
    work_date_year = models.ForeignKey(Year, on_delete=models.CASCADE,default=1)
    work_date_month = models.ForeignKey(Month, on_delete=models.CASCADE,default=1)
    work_date_day = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(31)])
    work_time = models.IntegerField()
    work_type =  models.CharField(choices=[(w.value, w.value) for w in WorkType],max_length=50)
    description = models.TextField()