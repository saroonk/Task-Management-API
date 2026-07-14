
from django.urls import path,include

from . import views



urlpatterns = [




    path('Register/' , views.Register.as_view() , name = 'register'),

    path('ManageUsers/<int:pk>/',views.ManageUsers.as_view() , name='ManageUsers'),





    path('Create_Admin/' , views.Create_Admin.as_view() , name = 'Create_Admin'),

    path('Delete_Admin/<int:pk>/' , views.Delete_Admin.as_view() , name = 'Delete_Admin'),


    path('users/<int:pk>/role/' , views.users_role.as_view() , name = 'users_role'),



    path('users/<int:pk>/promote/' , views.users_promote.as_view() , name = 'users_promote'),

    path('users/<int:pk>/demote/' , views.users_demote.as_view() , name = 'users_demote'),




    #TASK


    path('Task/' , views.TaskList.as_view() , name = 'task'),
    path('Task/<int:pk>/' , views.TaskManage.as_view() , name = 'TaskManage'),

    path('Task/<int:pk>/report/' , views.TaskReport.as_view() , name = 'TaskReport'),





    






    



    










]