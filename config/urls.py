from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
   openapi.Info(
      title="homework",
      default_version='v1',
      description="sayfullayev",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="1@gmail.com"),
      license=openapi.License(name="best"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('accounts_h/', include('users_h.urls')),
    path('accounts_m/', include('users_m.urls')),

    path('mijoz/', include('mijoz.urls')),
    path('hodim/', include('hodim.urls')),


    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]