from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    body = models.TextField()
    priority = models.IntegerField()

    def __str__(self):
        return self.name


class EducationalOrganizationModel(models.Model):
    name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubdivisionModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class ActivityModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PracticeModel(models.Model):
    name = models.CharField(max_length=255)
    subdivision = models.ForeignKey(SubdivisionModel, on_delete=models.SET_NULL, null=True)
    activity = models.ManyToManyField(ActivityModel)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name


