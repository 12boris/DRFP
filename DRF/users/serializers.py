from rest_framework.serializers import HyperlinkedModelSerializer
from .models import from rest_framework import serializers
from .models import CustomUser, Project CustomToDo
from rest_framework import serializers


class UserModelSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = CustomUser
		fields = '__all__'
		
class ProjectModelSerializer(HyperlinkedModelSerializer):
	Project = ProjectModelSerializer()
	
	class Meta:
		model = Project
		fields = '__all__'

class ToDoModelSerializer(HyperlinkedModelSerializer):
	ToDo = ProjectModelSerializer()
	
	class Meta:
		model = CustomToDo
		fields = '__all__'
		
		
		
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = '__all__'
		
class ToDoSerializerBase(serializers.ModelSerializer):
	class Meta:
		model = CustomToDo
		fields = '__all__'
		
class PrijectSerializerBase(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'
		
class ProjectSerializer(serializers.ModelSerializer):
	Project = ProjectSerializer()
	class Meta:
		model = Project
		fields = '__all__
		
class ToDoSerializer(serializers.ModelSerializer):
	ToDo = ToDoSerializer()
	class Meta:
		model = CustomToDo
		fields = '__all__
		
