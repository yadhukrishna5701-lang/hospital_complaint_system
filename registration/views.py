from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from django.db.models import Count
from registration.serializers import UserSerializer,ComplaintSerializer
from registration.models import Complaint



class SingUpview(APIView):
    def post(self,request):
        form_data = request.data
        serializers_instance = UserSerializer(data = form_data)

        if serializers_instance.is_valid():
            cleaned_data = serializers_instance.validated_data

            instance = User.objects.create_user(**cleaned_data)
            serializers_instance=UserSerializer(instance)

            return Response(data= serializers_instance.data)
        else:
            return Response(data=serializers_instance.errors)


class ComplaintListCreateViews(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        instance = Complaint.objects.filter(user=request.user)
        serializer_instance = ComplaintSerializer(instance,many = True)
        return Response(data = serializer_instance.data)

    def post(self,request):
        form_data = request.data 
        serializer_instance = ComplaintSerializer(data = form_data)

        if serializer_instance.is_valid():
            serializer_instance.save(user = request.user)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


class ComplaintRetrieveUpdateDeleteViews(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk=None):
        instance = get_object_or_404(Complaint,id=pk)
        self.check_object_permissions(request,instance)
        serializer_instance = ComplaintSerializer(instance)
        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):
        instance = get_object_or_404(Complaint,id=pk)
        self.check_object_permissions(request,instance)
        form_data = request.data
        serializer_instance = ComplaintSerializer(data= form_data,instance=instance)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):
        instance = get_object_or_404(Complaint,id=pk)
        self.check_object_permissions(request,instance)
        instance.delete()
        return Response(data={"message":"deleted"})

class SummaryView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        unresolved_complaints = Complaint.objects.filter(user=request.user).exclude(status='Resolved')
        serializer_instance = ComplaintSerializer(unresolved_complaints,many=True)
        return Response (data=serializer_instance.data)

class totalView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get (self,request):
        total = Complaint.objects.filter(user=request.user).count()
        return Response({"total_complaints":total})

class Group_by(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        group_by = Complaint.objects.values("status").annotate(count=Count("id"))

        return Response(group_by)
class Priority(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        priority = Complaint.objects.filter(priority__in=["High","Critical"])
        serializer_instance = ComplaintSerializer(priority,many=True)
        return Response(serializer_instance.data)