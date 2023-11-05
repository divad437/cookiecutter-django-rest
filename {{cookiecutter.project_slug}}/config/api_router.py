from django.urls import path, include
from rest_framework.routers import DefaultRouter
{%- if cookiecutter.use_simplejwt == 'y' %}
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
{%- endif %}

from {{ cookiecutter.project_slug }}.users.views import UserViewSet


router = DefaultRouter()

router.register("users", UserViewSet)


app_name = "api"

urlpatterns = [
{%- if cookiecutter.use_djoser == 'y' %}
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
{%- else %}
{%- if cookiecutter.use_simplejwt == 'y' %}
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
{%- endif %}
{%- endif %}
]

urlpatterns += router.urls
