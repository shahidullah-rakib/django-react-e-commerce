from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SuperAdminRegisterView, OperatorRegisterView, CustomerRegisterView, CustomerProfileView

urlpatterns = [
    path('admin/register/', SuperAdminRegisterView.as_view(), name='admin-register'),
    path('operator/register/', OperatorRegisterView.as_view(), name='operator-register'),
    path('customer/register/', CustomerRegisterView.as_view(), name='customer-register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('customer/profile/', CustomerProfileView.as_view(), name='customer-profile'),
]
