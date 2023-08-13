from django.urls import path , include
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tinymce/', include('tinymce.urls')),
    path('admin/report', views.report, name='report'),
    path('admin/report/results', views.report_results, name='report_results'),
    path('work_report/add/',views.add_employee_work_report, name='add_employee_work_report'),
]


admin.site.site_header  =  "Mini HR administration Panel"  
admin.site.site_title  =  "Mini HR Programmer"
admin.site.index_title  =  "Mini HR Dashboard"
