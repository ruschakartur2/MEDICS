from django.contrib import admin
from django.urls import path, include

from pations.views import HomePage, CreatePatiant

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add/', CreatePatiant.as_view(),name='add'),

]
