# Create your views here.

from authentication.serializers import (
    UserModelSerializerIn,
    UserModelSerializerOut,
    UserModelSerializerUpdate,
    UserSerializerOut,
)
from authentication.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import requests
# users = [{"name": "hamza", "age": 21}, {"name": "youssef", "age": 12}]


@api_view(
    [
        "GET",
        "POST",
    ]
)
def home(request):
    return Response({"message": "Hello World 4"})

@api_view(
    [
        "GET",
    ]
)
def test_url(request):
    url = request.query_params.get("url")
    print(url)
    req =  requests.get(url)
    return Response({"message": req.status_code})


@api_view(["GET", "POST"])
def UsersView(request):
    # users = []
    # for user in User.objects.all():
    #     users.append(user.getInfo())

    if request.method == "GET":
        users = User.objects.all()
        ser = UserModelSerializerOut(users, many=True)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(ser.data)

    elif request.method == "POST":
        user_info = request.data
        ser = UserModelSerializerIn(data=user_info)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


@api_view(["GET", "PATCH"])
def UserDetail(request, name):
    user = get_object_or_404(User, username=name)

    if request.method == "GET":
        ser = UserModelSerializerOut(user)
        return Response(ser.data)

    elif request.method == "PATCH":
        data = request.data
        ser = UserModelSerializerUpdate(user, data=data, partial=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)
