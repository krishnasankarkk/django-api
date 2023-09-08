from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class ReactView(APIView):
    
    def get(self, request):
        detail = {
            "name": "Kichu", "age": 23
        }
        return Response(detail)
