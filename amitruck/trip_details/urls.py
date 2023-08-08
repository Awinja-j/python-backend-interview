# trip_details/urls.py

from django.urls import path
from .views import TripDetailsView
from rest_framework.authtoken import views


urlpatterns = [
    path('api/log_trip/', TripDetailsView.as_view(), name='log_trip'),
    path('api-token-auth/', views.obtain_auth_token),
]
