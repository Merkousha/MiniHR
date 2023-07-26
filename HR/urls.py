from django.urls import path , include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf.urls.static import static 
from django.conf import settings  
from django.contrib import admin
from .views import home, report, report_results


urlpatterns = [
    path('', home, name='home'),
    path('tinymce/', include('tinymce.urls')),
    path('admin/report', report, name='report'),
    path('admin/report/results', report_results, name='report_results'),
]


admin.site.site_header  =  "Mini HR administration Panel"  
admin.site.site_title  =  "Mini HR Programmer"
admin.site.index_title  =  "Mini HR Dashboard"
