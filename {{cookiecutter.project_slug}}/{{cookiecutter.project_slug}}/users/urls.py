from rest_framework.routers import DefaultRouter

from {{ cookiecutter.project_slug }}.users.views import UserViewSet


router = DefaultRouter()

router.register("", UserViewSet, basename="users")


urlpatterns = router.urls
