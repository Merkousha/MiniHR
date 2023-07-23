from HR.models.employeetype import EmployeeType
from HR.models.gender import Gender
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=20)    
    last_name = models.CharField(max_length=50)    
    gender=models.ForeignKey(Gender, on_delete=models.CASCADE,default=1)   
    employee_type=models.ForeignKey(EmployeeType, on_delete=models.CASCADE,default=1)   
    birth_date = models.DateField()
    join_date = models.DateField()
    is_active = models.BooleanField()