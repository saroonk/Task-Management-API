from django.db import models
from django.contrib.auth.models import User




class Task(models.Model):

    user = models.ForeignKey(User , on_delete=models.SET_NULL, null=True, related_name='manager')

    choices = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    Title =  models.CharField(max_length=100)
    description =  models.TextField()
    Assigned_To = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_task')
    Due_Date = models.DateField()
    Status = models.CharField(max_length=20, choices=choices, default='Pending')
    Completion_Report = models.TextField(blank=True, null=True)
    Worked_Hours = models.PositiveIntegerField(blank=True, null=True)







class AdminAssignment(models.Model):
    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="assigned_users"
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="assigned_admin"
    )


    class Meta:
        unique_together = ('admin', 'user')