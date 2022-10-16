from .models import QueryBuilder
from rest_framework.decorators import api_view
from django.http import JsonResponse
from datetime import date

# search experiences
@api_view(['GET'])
def get_experiences(request):
    city = request.GET.get('city')
    # "2011-01-01"
    start_date = date.today()
    if request.GET.get('start_date'):
        start_date = request.GET.get('start_date')

    end_date = request.GET.get('end_date')

    # build dict for params
    params = {}
    if city:
        params['city'] = city
    if start_date:
        params['start_date'] = start_date
    if end_date:
        params['end_date'] = end_date

    # instantiate new QueryBuilder and execute
    query = QueryBuilder("experience", params, "get")
    result = query.execute()

    return JsonResponse({'data': result, 'keyword': {
        'city': city,
        'start_date': start_date,
        'end_date': end_date
    }})

# add interest to an experience
@api_view(['POST'])
def add_interest(request):
    experience_id = request.data.get('experience_id')
    user_id = request.user['id']

    # build dict for params
    params = {}
    params['experience_id'] = experience_id
    params['user_id'] = user_id

    # instantiate new QueryBuilder for post and execute
    query = QueryBuilder("interest", params, "post")
    result = query.execute()

    return JsonResponse({'data': result})

# get interests of a user
@api_view(['GET'])
def get_interests(request):
    user_id = request.GET.get('user_id') # not logged in user: used to fetch friend's interests

    # build dict for params
    params = {}
    if user_id:
        params['user_id'] = user_id
    else:
        return JsonResponse({'error': 'User id missing'}, status=400)

    # instantiate new QueryBuilder and execute
    query = QueryBuilder("get-interest", params, "get")
    result = query.execute()

    return JsonResponse({'data': result})

# search users by username prefix
@api_view(['GET'])
def search_users(request):
    prefix = request.GET.get('prefix')

    user_id = request.user['id']

    # build dict for params
    params = {}
    params['prefix'] = prefix
    params['user_id'] = user_id

    # instantiate new QueryBuilder and execute
    query = QueryBuilder("get-user", params, "get")
    result = query.execute()

    return JsonResponse({'data': result})

# user check route: get user from token and store if not exists
@api_view(['GET'])
def check_user(request):
    user = request.user
    firebase_user = request.firebase_user
    if not user:
        data = {'email': firebase_user.email, 'name': firebase_user.display_name, 'image': firebase_user.photo_url, 'level': 0}
        # instantiate new QueryBuilder for post and execute
        query = QueryBuilder("user", data, "post")
        result = query.execute()
        return JsonResponse({'data': result})
    
    return JsonResponse({'data': user})

# add follower
@api_view(['POST'])
def add_follower(request):
    following_id = request.GET.get('user_id')
    user_id = request.user['id']
    if not following_id:
        return JsonResponse({'error': 'follower not found'}, status=404)
    
    query = QueryBuilder("useraddfollow", {'following_id': following_id, 'user_id': user_id}, "post")
    query.execute()
    
    return JsonResponse({'msg': 'success'})

@api_view(['POST'])
def remove_follower(request):
    following_id = request.GET.get('user_id')
    user_id = request.user['id']
    if not following_id:
        return JsonResponse({'error': 'follower not found'}, status=404)
    
    query = QueryBuilder("userremfollow", {'following_id': following_id, 'user_id': user_id}, "post")
    query.execute()

    return JsonResponse({'msg': 'success'})


@api_view(['POST'])
def add_comment(request):
    user_id = request.user['id']
    experience_id = request.data.get('experience_id')
    comment_text = request.data.get('comment_text')

    if comment_text and experience_id:
        data = {'user_id': user_id, 'experience_id': experience_id, 'comment_text': comment_text}
        query = QueryBuilder("comment", data, "post")
        result = query.execute()
        return JsonResponse({'data': result})
    else:
        return JsonResponse({'error': 'empty params'}, status=400)

@api_view(['GET'])
def get_comments(request):
    experience_id = request.data.get('experience_id')

    query = QueryBuilder("get-comment", {'experience_id': experience_id}, "get")
    result = query.execute()

    return JsonResponse({'data': result})

@api_view(['GET'])
def get_users_with_stories(request):
    user_id = request.user['id']

    query = QueryBuilder("userwithstories", {'user_id': user_id}, "get")
    result = query.execute()

    return JsonResponse({'data': result})
