from rest_framework.views import APIView
from rest_framework.response import Response



class HelloAPIView(APIView):
    """ Test API View """
    def get(self, request, format=None):
        """ Return a list of APIView features """
        an_apiview = [
            'users HTTP methods as function get post patch put delete',
            'Is similar to a traditional django views',
            'Gives you the most control over you application logic',
            'Test Test Test ',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
