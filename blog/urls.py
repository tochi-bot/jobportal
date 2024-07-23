from django.urls import path
from .views import BlogListView, post_detail
from . import views  # Import views from the current module


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]


