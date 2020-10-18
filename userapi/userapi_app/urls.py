from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from userapi_app import views

urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
]
