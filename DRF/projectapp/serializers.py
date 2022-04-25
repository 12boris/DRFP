from rest_framework.serializers import ModelSerializer
from .models import Project


class ArticleSerializer(ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'
