from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('create/',create,name='create'),
    path('edit/<int:pk>/',edit,name='edit')
]