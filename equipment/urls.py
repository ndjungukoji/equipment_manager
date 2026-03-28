<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),
    path('<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('new/', views.equipment_create, name='equipment_create'),
]
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.equipment_list, name='equipment_list'),
    path('<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('new/', views.equipment_create, name='equipment_create'),
]
>>>>>>> 5bd48501490524661776bca42704bc3a758b0c75
