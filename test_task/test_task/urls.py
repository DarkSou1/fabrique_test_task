from rest_framework import permissions

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Фабрира Решений.',
        default_version='v1',
        description='Тестовое задание для Фабрики решений.',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='contact@fabric.local'),
        license=openapi.License(name='BSD Lisense')
    ), public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('api/', include('test_api.urls')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',
                                      cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0),
         name='schema-redoc'),
]
