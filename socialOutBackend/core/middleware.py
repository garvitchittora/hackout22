import firebase_admin
from firebase_admin import credentials
from django.http import JsonResponse
from firebase_admin import auth 
from .models import QueryBuilder
from .config import ANALYTICS
from .models import Analytics

class AuthMiddleware:
    def __init__(self, get_response):
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        self.get_response = get_response
    
    def __call__(self, request):
        try:
            if "admin" not in request.path:
                token = request.headers.get('Authorization')
                decoded_token = auth.verify_id_token(token)
                uid = decoded_token['uid']
                firebase_user = auth.get_user(uid)
                email = firebase_user.email
                
                query = QueryBuilder("user", {'email': email}, "get")
                result = query.execute()

                request.user = result
                request.firebase_user = firebase_user
            response = self.get_response(request)
            return response
        except Exception as e:
            return JsonResponse({'error': 'Unauthorized: ' + str(e)}, status=401)

# analytics middleware which identifies url 
class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        experience_id = request.headers.get('experience_id')
        if experience_id:
            if Analytics.objects.filter(type=Analytics[request.path], reference=request.query_params['experience_id']).exists():
                analytics = Analytics.objects.get(type=Analytics[request.path], reference=request.query_params['experience_id'])
                analytics.count += 1
                analytics.save()
            else:
                analytics = Analytics(type=Analytics[request.path], count=1, reference=request.query_params['experience_id'])
                analytics.save()
        response = self.get_response(request)
        return response