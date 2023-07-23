from HR.models.weekday import WeekDay
from HR.models.year import Year
from django.db import models

class Month(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE,default=1)   
    name = models.CharField(max_length=20)    
    dayscount = models.DecimalField(max_digits=5, decimal_places=2)
    start_day =models.ForeignKey(WeekDay, on_delete=models.CASCADE,default=1)   
    def __str__(self):
        return self.name