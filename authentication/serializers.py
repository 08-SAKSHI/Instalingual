from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from models import RegisterUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['new_user','gender','DOB','occupation','mother_tongue','phone_number','Future_goals']