from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="home"),
    path('trabajos/', views.works_view, name="works")
]