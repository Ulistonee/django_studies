from django.urls import path
from django.conf.urls import url
from .views import HomePageView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^success', views.success, name='success'),
]
