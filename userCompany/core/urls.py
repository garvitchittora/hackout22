from django.urls import path
from .views import *
from .post_views import *

urlpatterns = [
    path("", ListCountryAPIView.as_view()),
    path("experience/", ListExperienceAPIView.as_view()),
    path("get-interest/", ListInterestAPIView.as_view()),
    path("interest/", add_interest),
    path("get-user/", ListUserAPIView.as_view()),
    path("user/", create_user),
    path("useraddfollow/", add_follower),
    path("userremfollow/", remove_follower),
    path("comment/", add_comment),
    path("get-comment/", ListCommentAPIView.as_view()),
    path("userwithstories/", user_with_stories)
]