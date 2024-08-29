from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import SignUpView, UserListCreateView, UserDetailView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', UserListCreateView.as_view(), name='user-list-create'), #we use empty quotes to allow api redirection to /users
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]


