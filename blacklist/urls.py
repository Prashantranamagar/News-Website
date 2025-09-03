from django.urls import path
from . import views

urlpatterns = [
    path("blacklist/", views.black_list, name="black_list"),
    path("blacklist/add/", views.ip_add, name="ip_add"),
    path("blacklist/del/<int:pk>/", views.ip_del, name="ip_del"),
]
