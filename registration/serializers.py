from rest_framework import serializers
from django.contrib.auth.models import User
from registration.models import Complaint

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id","username","email","password"]

        read_only_fields = ["id"]

class ComplaintSerializer(serializers.ModelSerializer):

    class Meta:

        model = Complaint
        fields = "__all__"
        read_only_fields = ["id","user","reported_date"]