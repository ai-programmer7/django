from django.urls import path
from . import views

urlpatterns = [
    path("", views.MiniProfileView.as_view(), name='main')
]