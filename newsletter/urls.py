from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/add/', views.news_letter, name='news_letter'),
    path('panel/newsletter/emails/', views.news_emails, name='news_emails'),
    path('panel/newsletter/phones/', views.news_phones, name='news_phones'),
    path('panel/newsletter/del/<int:pk>/<int:num>/', views.news_txt_del, name='news_txt_del'),
]
