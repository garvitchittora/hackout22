from django.urls import path
from .views import *

urlpatterns = [
    path('test/', search_users),
    path('experience/', get_experiences),
    path('add_interest/', add_interest),
    path('get_interests/', get_interests),
    path('search/', search_users),
    path('check/', check_user),
    path('follow/', add_follower),
    path('unfollow/', remove_follower),
    path('add_comment/', add_comment),
    path('get_comments/', get_comments),
    path('get_story_users/', get_users_with_stories),
]
