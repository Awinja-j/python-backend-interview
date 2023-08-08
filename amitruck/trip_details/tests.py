from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .models import Trip
from .views import TripDetailsView

class TripDetailsAPITest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_successful_trip_creation(self):
        api_token = 'your_valid_api_token'
        data = {
            'driver_id': 1,
            'vehicle_id': 1,
            'customer_id': 1,
            'address': '123 Main St',
            'cargo_tonnage': 5.0,
            'address_type': 'pickup_point',
            'done_by_user_id': 'user_uuid',
        }
        request = self.factory.post('/api/log_trip/', data, format='json', HTTP_API_TOKEN=api_token)
        response = TripDetailsView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unauthorized_request(self):
        request = self.factory.post('/api/log_trip/', format='json')
        response = TripDetailsView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_missing_required_fields(self):
        api_token = 'your_valid_api_token'
        data = {
            'driver_id': 1,
            'vehicle_id': 1,
            'customer_id': 1,
            'address': '123 Main St',
            'cargo_tonnage': 5.0,
            # Missing 'address_type' and 'done_by_user_id'
        }
        request = self.factory.post('/api/log_trip/', data, format='json', HTTP_API_TOKEN=api_token)
        response = TripDetailsView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Add more test cases as needed

    # Test case for capturing trip details with a database mock
    def test_capture_trip_with_mock_database(self):
        class MockTrip:
            def __init__(self):
                self.trip = None

            def create(self, **data):
                self.trip = Trip(**data)
                self.trip.id = 1
                return self.trip

        mock_trip = MockTrip()

        api_token = 'your_valid_api_token'
        data = {
            'driver_id': 1,
            'vehicle_id': 1,
            'customer_id': 1,
            'address': '123 Main St',
            'cargo_tonnage': 5.0,
            'address_type': 'pickup_point',
            'done_by_user_id': 'user_uuid',
        }
        request = self.factory.post('/api/log_trip/', data, format='json', HTTP_API_TOKEN=api_token)
        response = TripDetailsView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(mock_trip.trip.id, 1)  # Check if the trip was captured

# Add more test cases as needed
