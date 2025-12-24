from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('articles/')),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
