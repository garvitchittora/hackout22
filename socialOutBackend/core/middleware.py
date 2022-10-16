import firebase_admin
from firebase_admin import credentials
from django.http import JsonResponse
from firebase_admin import auth 
from .models import QueryBuilder

class AuthMiddleware:
    def __init__(self, get_response):
        cred = credentials.Certificate("serviceAccountKey.json")
        firebase_admin.initialize_app(cred)
        self.get_response = get_response
    
    def __call__(self, request):
        try:
            if "admin" not in request.path:
                # token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjVkMzQwZGRiYzNjNWJhY2M0Y2VlMWZiOWQxNmU5ODM3ZWM2MTYzZWIiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVmFydW4gVGl3YXJpIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FMbTV3dTNjN2hiRWFwc0dqSUJscUhvQWRpRktfSThvaUdXdjRvbnZQdWQ1TXc9czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vc29jaWFsb3V0LTZkNjE2IiwiYXVkIjoic29jaWFsb3V0LTZkNjE2IiwiYXV0aF90aW1lIjoxNjY1NzgyMDUxLCJ1c2VyX2lkIjoiM1J3QXZLOVJRTVFhc3FvTVVBTTR4RmZRalhJMyIsInN1YiI6IjNSd0F2SzlSUU1RYXNxb01VQU00eEZmUWpYSTMiLCJpYXQiOjE2NjU3ODIwNTIsImV4cCI6MTY2NTc4NTY1MiwiZW1haWwiOiJ2YXJ1bi4yMDExdEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjExMDYwNzQyNzAyMjUyNDYwNTExNiJdLCJlbWFpbCI6WyJ2YXJ1bi4yMDExdEBnbWFpbC5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJnb29nbGUuY29tIn19.uK7zak0xN_k6Xl3act_s3H9GzzgGnhqCpLJJMTSDMaEx2u-sQt__3EvvmwUYKIcjE6WKUTKgXjgYHMe28J8tfA2YP75pTUdpAxJPIV9PR6IRwpL0yY_sUQSRvopM_5JhOLuRPqNT7xVI_Lk7ZnAxdrPKZJfLTx2-HwAkP-88Ft3cLFcsV0_gP2sApbR9T9_NEV1e_bB0qPETIXxcZW9aFtAZWofTRXNRJ-zs_l2SREXaXsQRLTp-flUcQvx58QWATX5DQeIjJ5G0NzLvpu93wGWdYr41f_B7KnlCTYwguNX8CzcrwlzlO_0Lrvi1aFBJ6spMNJcMCrJArADcfoyLaQ"
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

