from django.shortcuts import render

# Create your views here.



from TaskAPP.models import *

from rest_framework.views import APIView

from rest_framework.generics import *

from .serializer import *

from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated

from .permission import SuperAdmin

from rest_framework.response import Response
from rest_framework import status

from rest_framework.exceptions import ValidationError



class Register(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [SuperAdmin]

    def get_queryset(self):
        return User.objects.filter(is_superuser = False , is_staff = False)


class ManageUsers(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ManageUserSerializer
    permission_classes = [SuperAdmin]

    def destroy(self,*args,**kwargs):
        instance = self.get_object()

        self.perform_destroy(instance)

        return Response(
            {
                "Message" : "Your Profile Has Benn Deleted Succesfully"
            }
        )










class Create_Admin(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateAdminSerializer
    permission_classes = [SuperAdmin]


    def get_queryset(self):
        return User.objects.filter(is_staff = True)




class Delete_Admin(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = DeleteAdminSerializer
    permission_classes= [SuperAdmin]




class users_role(UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = userroleserializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)

        user = self.get_object()
        role = request.data.get("role")

        return Response(
            {
                "message": f"{user.username}'s role has been changed to {role}.",
                "username": user.username,
                "role": role,
            },
            status=status.HTTP_200_OK,
        )



class users_promote(APIView):
    queryset = User.objects.all()
    serializer_class = users_promoteSerializer
    permission_classes = [SuperAdmin]

    def post(self,request, pk):
        user = get_object_or_404(User , pk = pk)


        if user == self.request.user:
            return Response({
                "Message" : "You Cant promote yourself"
            })
        
        elif user.is_staff and user.is_superuser:
            return Response({
                "Message" : "You are already a superuser"
            })
            

        elif user.is_staff and not user.is_superuser:
            user.is_superuser = True
            user.save()
            return Response({
                "Message" : "You have been promoted to superuser from admin"
            })

        elif not user.is_staff and not user.is_superuser:
            user.is_staff = True
            user.save()
            return Response({
                "Message" : "You have been promoted to Admin from User"
            })
       



class users_demote(APIView):
    queryset = User.objects.all()
    serializer_class = users_demoteSerializer
    permission_classes = [SuperAdmin]

    def post(self,request, pk):
        user = get_object_or_404(User , pk = pk)


        if user == self.request.user:
            return Response({
                "Message" : "You Cant demote yourself"
            })
        
        elif user.is_staff and user.is_superuser:
            user.is_superuser = False
            user.save()
            return Response({
                "Message" : "You are demote to admin from superuser"
            })
            

        elif user.is_staff and not user.is_superuser:
            user.is_staff = False
            user.save()
            return Response({
                "Message" : "You have been demote to User from admin"
            })

        elif not user.is_staff and not user.is_superuser:
         
            return Response({
                "Message" : "You are already at the lowest level, cant demote anymore"
            })





















class TaskList(ListCreateAPIView):
    queryset =  Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            query = Task.objects.all()
        elif user.is_staff:
            query = Task.objects.filter(user = user)
        else:
            query = Task.objects.filter(Assigned_To = user)

        return query

class TaskManage(RetrieveUpdateDestroyAPIView):
    queryset =  Task.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            query = Task.objects.all()
        elif user.is_staff:
            query = Task.objects.filter(user = user)
        else:
            query = Task.objects.filter(Assigned_To = user)

        return query

    def get_serializer_class(self):
        user = self.request.user

        if not user.is_superuser and not user.is_staff:
            return UserTaskUpdateSerializer

        return TaskManageSerializer



class TaskReport(RetrieveAPIView):

    queryset= Task.objects.all()
    serializer_class = TaskReportSerializer

    permission_classes = [IsAuthenticated,IsAdminUser]



    def get_object(self):
        task = super().get_object()

        if task.Status != "Completed":
            raise ValidationError({
                "message": "This task has not been completed yet."
            })

        return task