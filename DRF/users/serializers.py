from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Author
		fields = '__all__'
		
class ProjectModelSerializer(HyperlinkedModelSerializer):
	User = ProjectModelSerializer()
	
	class Meta:
		model = Author
		fields = '__all__'

class ToDoModelSerializer(HyperlinkedModelSerializer):
	User = ProjectModelSerializer()
	
	class Meta:
		model = Author
		fields = '__all__'
