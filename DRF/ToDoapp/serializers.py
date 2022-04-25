from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ToDo

class AuthorModelSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = ToDo
		fields = '__all__'
