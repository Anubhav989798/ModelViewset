from rest_framework.response import Response
from rest_framework import status

class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_exception(self,request,exception):
        msg=exception
        return Response({'error':msg},status=status.HTTP_400_BAD_REQUEST)