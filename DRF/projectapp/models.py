from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
	name = models.CharField(max_length=64)
	link = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name
