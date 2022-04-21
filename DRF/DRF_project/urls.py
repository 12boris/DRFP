from rest_framework.generics import UpdateAPIView
from django.urls import path, include
from mainapp import views
from rest_framework.routers import DefaultRouter
from rest_framework.generics import DestroyAPIView


router = DefaultRouter()
router.register('base', views.ArticleViewSet, basename='article')
filter_router = DefaultRouter()
filter_router.register('param', views.ArticleParamFilterViewSet)

urlpatterns = [
	path('viewsets/', include(router.urls)),
	path('filters/kwargs/<str:name>/', views.ArticleKwargsFilterView.as_view()),
	path('filters/', include(filter_router.urls)),
	path('generic/retrieve/<int:pk>/', views.ArticleRetrieveAPIView.as_view())
]


class ArticleUpdateAPIView(UpdateAPIView):
	renderer_classes = [JSONRenderer]
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer
	
class ArticleDestroyAPIView(DestroyAPIView):
	renderer_classes = [JSONRenderer]
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer



