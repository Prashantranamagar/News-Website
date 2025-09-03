from django.urls import re_path, path
from . import views

urlpatterns = [
    # re_path(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail'),
    path("news/<str:category>/<str:word>/", views.news_detail, name="news_detail"),
    re_path(r"^panel/news/list/$", views.news_list, name="news_list"),
    re_path(r"^panel/news/add/$", views.news_add, name="news_add"),
    re_path(r"^panel/news/del/(?P<pk>\d+)/$", views.news_delete, name="news_delete"),
    re_path(r"^panel/news/edit/(?P<pk>\d+)word/$", views.news_edit, name="news_edit"),
    re_path(
        r"^panel/news/publish/(?P<pk>\d+)/$", views.news_publish, name="news_publish"
    ),
    re_path(r"^urls/(?P<pk>\d+)/$", views.news_detail_short, name="news_detail_short"),
    re_path(r"^all/news/(?P<word>.*)/$", views.news_all_show, name="news_all_show"),
]
