from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorModelSerializer

class AuthorModelViewSet(ModelViewSet):
	queryset = Author.objects.all()
	serializer_class = AuthorModelSerializer
	
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


	
