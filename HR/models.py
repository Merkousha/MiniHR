from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.utils.crypto import get_random_string
    
class WeekDay(models.Model):
    name = models.CharField(max_length=20)  
    def __str__(self):
        return self.name

class Year(models.Model):
    # refrence = models.ForeignKey(Refrence, on_delete=models.CASCADE,default=1)   
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Month(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE,default=1)   
    name = models.CharField(max_length=20)    
    dayscount = models.DecimalField(max_digits=5, decimal_places=2)
    start_day =models.ForeignKey(WeekDay, on_delete=models.CASCADE,default=1)   
    def __str__(self):
        return self.name

class Day(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE,default=1)   
    weekday = models.ForeignKey(WeekDay, on_delete=models.CASCADE,default=1)   
    day_work = models.BooleanField()
    day_of_month = models.IntegerField(choices=[(i, i) for i in range(1, 32)],default=1)
    def __str__(self):
        return str(self.day_of_month)

class Gender(models.Model):
    name = models.CharField(max_length=20)  
    def __str__(self):
        return self.name

class EmployeeType(models.Model):
    name = models.CharField(max_length=20)  
    def __str__(self):
        return self.name

        
class Employee(models.Model):
    first_name = models.CharField(max_length=20)    
    last_name = models.CharField(max_length=50)    
    gender=models.ForeignKey(Gender, on_delete=models.CASCADE,default=1)   
    employee_type=models.ForeignKey(EmployeeType, on_delete=models.CASCADE,default=1)   
    birth_date = models.DateField()
    join_date = models.DateField()
    is_active = models.BooleanField()
    
    
    
    
    