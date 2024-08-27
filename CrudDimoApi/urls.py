from django.urls import path
from . import views

urlpatterns = [
    path('custom-users',views.CustomUsersView.as_view()),
    path('custom-users/<int:pk>', views.SingleCustomUsersView.as_view()),
]