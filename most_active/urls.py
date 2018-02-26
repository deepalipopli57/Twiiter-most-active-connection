from django.conf.urls import url

from most_active import views

urlpatterns = [
    url(r'^', views.most_active_users, name='most active' )
]