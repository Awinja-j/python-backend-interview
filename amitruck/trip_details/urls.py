# trip_details/urls.py

from django.urls import path
from .views import TripDetailsView

urlpatterns = [
    path('api/log_trip/', TripDetailsView.as_view(), name='log_trip'),
]
