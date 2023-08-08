
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, throttling
from .models import Trip
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class TripDetailsView(APIView):
    throttle_classes = [throttling.UserRateThrottle]

    @method_decorator(csrf_exempt)  # Disabling CSRF protection for simplicity
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        # Authenticate request using api_token parameter
        api_token = request.query_params.get('api_token')
        if not api_token:
            return Response(
                {'status_code': status.HTTP_403_FORBIDDEN, 'status': 'Forbidden', 'description': 'Unauthorized request.'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Validate input data
        data = request.data
        required_fields = ['driver_id', 'vehicle_id', 'customer_id', 'address', 'cargo_tonnage', 'address_type', 'done_by_user_id']
        for field in required_fields:
            if field not in data:
                return Response(
                    {'status_code': status.HTTP_400_BAD_REQUEST, 'status': 'Bad Request', 'description': f'Missing {field} in request.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        # Capture trip details and save to the database
        try:
            trip = Trip.objects.create(**data)
        except Exception as e:
            return Response(
                {'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'status': 'Internal Server Error', 'description': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        # Return response payload with success status
        return Response(
            {'status_code': status.HTTP_200_OK, 'status': 'OK', 'description': 'Trip details captured successfully.'},
            status=status.HTTP_200_OK
        )
