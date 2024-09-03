from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import SignUpView, UserListCreateView, UserDetailView, Test

urlpatterns = [
    path('test', Test.as_view()),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', UserListCreateView.as_view(), name='user-list-create'), #we use empty quotes to allow api redirection to /users
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]


