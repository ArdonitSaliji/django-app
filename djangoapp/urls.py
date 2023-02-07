from django.contrib import admin
from django.urls import path, include
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
]
