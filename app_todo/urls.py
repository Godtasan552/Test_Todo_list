from django.urls import path
from .import views 

urlpatterns = [
    path('',views.indexPage, name='index'),
    path('wathtodo/',views.wathtodoPage, name='wathtodo')
]
