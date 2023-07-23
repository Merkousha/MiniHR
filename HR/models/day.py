from HR.models.weekday import WeekDay
from HR.models.month import Month
from django.db import models

class Day(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE,default=1)   
    weekday = models.ForeignKey(WeekDay, on_delete=models.CASCADE,default=1)   
    day_work = models.BooleanField()
    day_of_month = models.IntegerField(choices=[(i, i) for i in range(1, 32)],default=1)
    def __str__(self):
        return str(self.day_of_month)