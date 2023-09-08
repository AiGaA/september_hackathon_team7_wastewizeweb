from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_shop_directory, name='shop'),
    path('add_shop/', views.view_shop_directory, name='add_shop'),
]
