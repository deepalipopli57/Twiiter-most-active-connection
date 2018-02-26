from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('most_active_users/', include('most_active.urls'))
]
