from . import views
from django.urls import path

urlpatterns = [
    path('jobs_list/', views.jobs_list.as_view(), name='jobs_list'),
]