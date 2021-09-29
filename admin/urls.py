from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from shared.conf_services import schema_view, trigger_error


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += [
    path('/', include('core.urls'))
]


# JWT
urlpatterns += [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

# Sentry
urlpatterns += [
    path('sentry-debug/', trigger_error),
]

# Swagger/OpenAPI
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )


