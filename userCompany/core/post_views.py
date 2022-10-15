from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from django.http import JsonResponse

# add follower
@api_view(['POST'])
def add_follower(request):
    following_id = request.data.get('following_id')
    user_id = request.data.get('user_id')
    if not following_id and not user_id:
        return JsonResponse({'error': 'follower not found'}, status=404)
    
    following_user = User.objects.get(id = following_id)
    user = User.objects.get(id = user_id)

    if user and not following_user in user.following.all():
        user.following.add(following_user)

    return JsonResponse({'msg': 'success'})

@api_view(['POST'])
def remove_follower(request):
    following_id = request.data.get('following_id')
    user_id = request.data.get('user_id')
    if not following_id and not user_id:
        return JsonResponse({'error': 'follower not found'}, status=404)
    
    following_user = User.objects.get(id = following_id)
    user = User.objects.get(id = user_id)

    if user and following_user in user.following.all():
        user.following.remove(following_user)

    return JsonResponse({'msg': 'success'})


@api_view(['POST'])
def add_comment(request):
    user_id = request.data.get('user_id')
    user = User.objects.get(id = user_id)
    interest_id = request.data.get('interest_id')
    comment_text = request.data.get('comment_text')
    interest = Interest.objects.get(id=interest_id)

    if comment_text and interest_id and interest:
        comment = Comments(user = user, interest = interest, comment_text=comment_text)
        comment.save()
        return JsonResponse({'msg': 'comment added'})
    else:
        return JsonResponse({'error': 'interest not found'}, status=404)

@api_view(['POST'])
def create_user(request):
    email = request.data.get('email')
    name = request.data.get('name')
    image = request.data.get('image')
    user = User.objects.get(email=email)
    if not user.exists():
        user = User.objects.create(email=email, name=name, image=image)
    
    return JsonResponse({'data': user})

# add interest to an experience
@api_view(['POST'])
def add_interest(request):
    experience_id = request.data.get('experience_id')
    user_id = request.data.get('user_id')
    user = User.objects.get(id = user_id)
    experience = Experience.objects.get(id=experience_id)

    if not experience and not user:
        return JsonResponse({'msg': 'experience and user not found'}, 404)

    interest = Interest.objects.create(experience=experience, user=user)

    return JsonResponse({'data': interest})

@api_view(['GET'])
def user_with_stories(request):
    user_id = request.GET.get('user_id')
    user = User.objects.get(id = user_id)

    result_list = []

    for u in user.following.all():
        if Interest.objects.filter(user = u).count():
            result_list.append(u)
    
    return JsonResponse({'data': result_list})