from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('paytm/', include('paytm.urls')),
    path('admin/', admin.site.urls),
]
