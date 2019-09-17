from django.contrib import admin
from django.urls import path

from mainApp import views  

urlpatterns = [
    path('', views.StatisticsUrlListView.as_view(), name="statList"),
    path('admin/', admin.site.urls),
]
