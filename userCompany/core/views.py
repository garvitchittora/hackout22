from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import *
from .models import *
from datetime import date

class ListCountryAPIView(ListAPIView):
    serializer_class = CountrySerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    
    def get_queryset(self):
        queryset = self.model.objects
        if 'code' in self.request.query_params:
            code = self.request.query_params['code']
            queryset = queryset.filter(code=code)
        return queryset.order_by('id')

class CreateCountryAPIView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class UpdateCountryAPIView(UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class DeleteCountryAPIView(DestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class ListCityAPIView(ListAPIView):
    serializer_class = CitySerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    
    def get_queryset(self):
        queryset = self.model.objects
        if 'code' in self.request.query_params:
            code = self.request.query_params['code']
            queryset = queryset.filter(code=code)
        return queryset.order_by('id')

class CreateCityAPIView(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class UpdateCityAPIView(UpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class DeleteCityAPIView(DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ListExperienceAPIView(ListAPIView):
    serializer_class = ExperienceSerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    
    def get_queryset(self):
        city = self.request.query_params.get('city', None)
        start_date = self.request.query_params.get('start_date', date.today())
        end_date = self.request.query_params.get('end_date', None)
        inventory_result = Inventory.objects.filter(slot__gt=0, date__gte=start_date)

        if end_date:
            inventory_result = inventory_result.filter(date__lte=end_date)

        if city:
            inventory_result = inventory_result.filter(city__code=city)

        # filter unique experiences from inventory using set
        experience = set()
        for i in inventory_result:
            experience.add(i.experience)

        # convert set to list
        experience = list(experience)

        return experience

class CreateExperienceAPIView(CreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class UpdateExperienceAPIView(UpdateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class DeleteExperienceAPIView(DestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ListCommentAPIView(ListAPIView):
    serializer_class = CommentSerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    
    def get_queryset(self):
        queryset = self.model.objects
        if 'experience_id' in self.request.query_params:
            experience_id = self.request.query_params['experience_id']
            queryset = queryset.filter(experience__id=experience_id)
        
        return queryset.order_by('-id')

class CreateCommentAPIView(CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class UpdateCommentAPIView(UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class DeleteCommentAPIView(DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer

class ListUserAPIView(ListAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    
    def get_queryset(self):
        queryset = self.model.objects

        if 'email' in self.request.query_params:
            email = self.request.query_params['email']
            queryset = queryset.filter(email=email)
            return queryset

        if 'user_id' in self.request.query_params:
            user_id = self.request.query_params['user_id']
            queryset = queryset.filter(id=user_id)
            return queryset

        if 'prefix' in self.request.query_params:
            prefix = self.request.query_params['prefix']
            user_id = self.request.query_params['user_id']
            users = queryset.filter(name__istartswith=prefix).order_by('level')

            if user_id:
                active_user = queryset.get(id = user_id)
                if active_user:
                    for u in users:
                        if u in active_user.following.all():
                            u.following_status = True
                        else:
                            u.following_status = False
            
            return users

        return queryset

class CreateUserAPIView(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class UpdateUserAPIView(UpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class DeleteUserAPIView(DestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ListInterestAPIView(ListAPIView):
    serializer_class = InterestSerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    
    def get_queryset(self):
        queryset = self.model.objects
        if 'user_id' in self.request.query_params:
            user_id = self.request.query_params['user_id']
            queryset = queryset.filter(user__id=user_id)
            return queryset.order_by('id')
        return []

class CreateInterestAPIView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = InterestSerializer

class UpdateInterestAPIView(UpdateAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class DeleteInterestAPIView(DestroyAPIView):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
