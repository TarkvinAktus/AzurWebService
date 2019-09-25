from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from mainApp import views  

urlpatterns = [
    path('options/', views.options_upload, name="options"),
    path('', views.StatisticsUrlListView.as_view(), name="statList"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns