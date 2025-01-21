from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Call DRF's default exception handler first
    response = exception_handler(exc, context)

    # If DRF's handler couldn't handle the exception, create a custom response
    if response is None:
        response_data = {
            'error': str(exc),
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
        }
        response = Response(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response