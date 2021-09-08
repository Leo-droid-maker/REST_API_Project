from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from userapp.views import UserCustomViewSet
from todoapp.views import ProjectModelViewSet, ToDoModelViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()

router.register('projects', ProjectModelViewSet)
router.register('todos', ToDoModelViewSet, basename='todo')
router.register('users', UserCustomViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
    path('viewsets/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
