from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    @staticmethod
    def get():
        return Response('hello this is a test get response')
