from django.shortcuts import render
from rest_framework.decorators import api_view
from main.serializers import MemberSerializer, ActivitySerializer
from main.models import Member, Activity_Period
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def get_data(request):
    members = Member.objects.all()
    if members:
        serialized_data = MemberSerializer(members, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    return Response("No Data Available", status=status.HTTP_204_NO_CONTENT)

