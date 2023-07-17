from django.contrib import admin
from HR.models import Year,Month,WeekDay,Day,Employee, EmployeeType ,Day , Gender

class MonthInline(admin.TabularInline):
    model = Month
    extra = 12  
    
class YearModelAdmin(admin.ModelAdmin):
    inlines = [MonthInline]
    
class DayInline(admin.TabularInline):
    model = Day
    extra = 31  
class MonthModelAdmin(admin.ModelAdmin):
    inlines = [DayInline]    
    
admin.site.register(Year,YearModelAdmin)
admin.site.register(Month,MonthModelAdmin)
admin.site.register(WeekDay)
admin.site.register(Day)

admin.site.register(Gender)
admin.site.register(EmployeeType)
admin.site.register(Employee)

