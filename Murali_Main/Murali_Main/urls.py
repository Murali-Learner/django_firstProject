from django import urls
from django.contrib import admin

from django.urls import path,include

urlpatterns = [
    path("",include("Murali_App.urls")),
    path('admin/', admin.site.urls),
    # path('/login',include("Murali_App.urls"))
]
