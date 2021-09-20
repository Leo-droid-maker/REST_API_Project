from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view as schema_for_swagger_template_and_tests
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from userapp.views import UserCustomViewSet
from todoapp.views import ProjectModelViewSet, ToDoModelViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view_for_swagger_template = schema_for_swagger_template_and_tests(
    title='TODO_API',
    permission_classes=[IsAuthenticatedOrReadOnly]
)

schema_view = get_schema_view(
    openapi.Info(
        title="TODO",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[IsAuthenticatedOrReadOnly],
)

router = DefaultRouter()

router.register('projects', ProjectModelViewSet)
router.register('todos', ToDoModelViewSet, basename='todo')
router.register('users', UserCustomViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
    # path('viewsets/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('schema/', schema_view_for_swagger_template, name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}),
        name='swagger-ui'),
    path('redoc-ui/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}),
        name='redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
