from django.urls import path
from . import views

urlpatterns = [
    path('panel/category/list/', views.cat_list, name='cat_list'),
    path('panel/category/add/', views.cat_add, name='cat_add'),
    path('export/cat/csv/', views.export_cat_csv, name='export_cat_csv'),
    path('import/cat/csv/', views.import_cat_csv, name='import_cat_csv'),
    path('news/<str:category>/', views.category_page, name='category'),
]
