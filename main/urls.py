from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('panel/', views.panel, name='panel'),
    path('login/', views.mylogin, name='mylogin'),
    path('logout/', views.mylogout, name='mylogout'),
    path('panel/setting/', views.site_setting, name='site_setting'),
    path('panel/about/setting/', views.about_setting, name='about_setting'),
    path('contact/', views.contact, name='contact'),
    path('panel/change/pass/', views.change_pass, name='change_pass'),
    path('register/', views.myregister, name='myregister'),
]
