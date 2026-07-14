

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from TaskAPP.models import *

class TaskListSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ["Completion_Report","Worked_Hours"]
        



class TaskManageSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserTaskUpdateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "Status",
            "Completion_Report",
            "Worked_Hours",
        ]


    def validate(self, attrs):
        status = attrs.get('Status')
        report = attrs.get('Completion_Report')

        hour = attrs.get('Worked_Hours')

        if status == "Completed":

            if not report:
                raise serializers.ValidationError("Need Completion Report if status is completed")
            
            if not hour:
                raise serializers.ValidationError("Need worked hour if status is completed")

        return attrs





class TaskReportSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ["Status","Completion_Report","Worked_Hours"]



class RegisterSerializer(ModelSerializer):


    password = serializers.CharField(write_only=True )

    class Meta:
        model = User
        fields = ['id','username','email','password']

    
    def create(self,validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )

        return user


class ManageUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username' , 'email']




class CreateAdminSerializer(ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username' , 'email' , 'password' , 'is_staff']


    def create(self,validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            is_staff = True
        )

        return user



class DeleteAdminSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = []



class userroleserializer(ModelSerializer):

    role = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['role']

    def update(self,instance,validated_data):
        role = validated_data['role']

        if role == 'user':
            instance.is_staff = False
            instance.is_superuser = False
        elif role == 'admin':
            instance.is_staff = True
            instance.is_superuser = False
        elif role == 'superadmin':
            instance.is_staff = True
            instance.is_superuser = True
        instance.save()
        return instance

class users_promoteSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = []

    

class users_demoteSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = []