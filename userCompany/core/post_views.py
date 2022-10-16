from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from django.http import JsonResponse

# add follower
@api_view(['POST'])
def add_follower(request):
    following_id = request.data.get('following_id')
    user_id = request.data.get('user_id')
    if (not following_id) or (not user_id) or (following_id == user_id):
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
    if (not following_id) or (not user_id) or (following_id == user_id):
        return JsonResponse({'error': 'follower not found'}, status=404)
    
    following_user = User.objects.get(id = following_id)
    user = User.objects.get(id = user_id)

    if user and following_user in user.following.all():
        print("hello")
        user.following.remove(following_user)

    return JsonResponse({'msg': 'success'})


@api_view(['POST'])
def add_comment(request):
    user_id = request.data.get('user_id')
    user = User.objects.get(id = user_id)
    experience_id = request.data.get('experience_id')
    comment_text = request.data.get('comment_text')
    experience = Experience.objects.get(id=experience_id)

    if comment_text and experience and user:
        comment = Comments(user = user, experience = experience, comment_text=comment_text)
        comment.save()
        return JsonResponse({'msg': 'comment added'})
    else:
        return JsonResponse({'error': 'interest not found'}, status=404)

@api_view(['POST'])
def create_user(request):
    email = request.data.get('email')
    name = request.data.get('name')
    image = request.data.get('image')
    user = User.objects.filter(email=email)
    if not user.exists():
        user = User(email=email, name=name, image=image)
        user.save()
    return JsonResponse({'data': 'success'})

# add interest to an experience
@api_view(['POST'])
def add_interest(request):
    experience_id = request.data.get('experience_id')
    user_id = request.data.get('user_id')
    user = User.objects.get(id = user_id)
    experience = Experience.objects.get(id=experience_id)

    if not experience and not user:
        return JsonResponse({'msg': 'experience and user not found'}, 404)

    Interest.objects.create(experience=experience, user=user)

    return JsonResponse({'data': 'success'})

@api_view(['GET'])
def user_with_stories(request):
    user_id = request.GET.get('user_id')
    result_list = []
    if user_id:
        user = User.objects.get(id = user_id)

        for u in user.following.all():
            if Interest.objects.filter(user = u).count():
                result_list.append(UserSerializer(u).data)
    
    return JsonResponse({'data': result_list})