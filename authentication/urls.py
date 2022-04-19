from authentication.views import UserDetail, UsersView, home, test_url
from django.urls import path

urlpatterns = [
    path("home/", home),
    path("users/", UsersView),
    path("users/<str:name>", UserDetail),
]
