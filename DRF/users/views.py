from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from .models import CustomUser, CustomToDo, Project
from .serializers import ToDoSerializerBase, ProjectSerializerBase, ProjectSerializer, ToDoSerializer, UserSerializer



class AuthorViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = CustomUser.objects.all()
	
class ToDoViewSet(viewsets.ModelViewSet):
	serializer_class = ToDoSerializer
	queryset = CustomToDo.objects.all()
	
	def get_serializer_class(self):
		if self.request.method in ['GET']:
			return ToDoSerializer
		return ToDoSerializerBase
		
class ProjectViewSet(viewsets.ModelViewSet):
	serializer_class = ProjectSerializer
	queryset = Project.objects.all()
	
	def get_serializer_class(self):
		if self.request.method in ['GET']:
			return ProjectSerializer
		return ProjectSerializerBase



class UserModelViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserModelSerializer
	
@api_view(['GET'])
@renderer_classes([JSONRenderer])
def article_view(request):
	articles = Article.objects.all()
	serializer = ArticleSerializer(articles, many=True)
	return Response(serializer.data)
	
class ArticleListAPIView(ListAPIView):
	renderer_classes = [JSONRenderer]
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	
class ArticleViewSet(viewsets.ViewSet):
	renderer_classes = [JSONRenderer]
	@action(detail=True, methods=['get'])
	def article_text_only(self, request, pk=None):
		article = get_object_or_404(Article, pk=pk)
		return Response({'article.text': article.text})
	def list(self, request):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		return Response(serializer.data)
	def retrieve(self, request, pk=None):
		article = get_object_or_404(Article, pk=pk)
		serializer = ArticleSerializer(article)
		return Response(serializer.data)

class ArticleDjangoFilterViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	filterset_fields = ['name', 'user']

class ArticleCustomDjangoFilterViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	filterset_class = ArticleFilter

class ArticleLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 2
	
class ArticleLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	pagination_class = ArticleLimitOffsetPagination
	
