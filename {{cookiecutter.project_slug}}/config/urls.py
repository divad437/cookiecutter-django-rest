from django.conf import settings
{%- if cookiecutter.use_async == 'y' %}
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
{%- endif %}
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
{% if cookiecutter.use_djoser == 'n' and cookiecutter.use_simplejwt == 'n' %}
    path("auth-token/", obtain_auth_token),
{% endif %}
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
{%- if cookiecutter.use_djoser == 'y' %}
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
{%- else %}
{%- if cookiecutter.use_simplejwt == 'y' and cookiecutter.use_djoser == 'y' %}
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
{%- endif %}
{%- endif %}
    path("api/users/", include("{{ cookiecutter.project_slug }}.users.urls")),
]

{%- if cookiecutter.use_async == 'y' %}
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
{%- endif %}
