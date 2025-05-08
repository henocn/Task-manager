from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from main.views import TaskViewSet, CategoryViewSet, UserTasksView


# Configuration de Swagger/OpenAPI
schema_view = get_schema_view(
   openapi.Info(
      title="Gestionnaire de Tâches API",
      default_version='v1',
      description="API pour gérer vos tâches quotidiennes",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ngasamah@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Initialisation du routeur DRF
router = routers.DefaultRouter()
router.register(r'taches', TaskViewSet, basename='tache')
router.register(r'categories', CategoryViewSet)
router.register(r'mes-taches', UserTasksView, basename='mes-taches')

urlpatterns = [
    # Administration Django
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    # Documentation API
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Authentification JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
