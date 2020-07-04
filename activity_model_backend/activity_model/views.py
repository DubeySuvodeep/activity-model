from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

from activity_model.models import User, ActivityPeriod
from activity_model.serializers import ReadActivitySerializer, ReadUserSerializer
# Create your views here.

class UserDetail(APIView):

    def get(self, request):
        try:
            members = User.objects.all()
            print(members)
            serializer = ReadUserSerializer(members, many=True)
            print(serializer)
            return Response({"ok": True, "members": serializer.data})
        except Exception as e:
            print(e)