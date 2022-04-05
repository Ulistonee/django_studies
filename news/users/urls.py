from django.urls import path
from .views import SignUpView
from django.conf.urls import url
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    url(r'^$', views.index, name='index'),
    url(r'^success', views.success, name='success'),
]
