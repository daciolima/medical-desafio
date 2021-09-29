from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# conf serviço da interface Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny]
)


# Return falha no sentry
def trigger_error(request):
    division_by_zero = 1 / 0

