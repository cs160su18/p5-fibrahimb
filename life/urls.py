from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/', views.schedule, name='schedule_listing'),
    path('send/', views.send, name='send'),
    path('jobs/', views.jobs, name='jobs'),
    path('listings/', views.listings, name='job_listing'),
    path('applications/', views.applications, name='applications'),
    path('admin/', admin.site.urls),
    path('life/', include('django.contrib.auth.urls')),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
