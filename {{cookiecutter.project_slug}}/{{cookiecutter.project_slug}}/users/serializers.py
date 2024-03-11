from django.contrib.auth import get_user_model
from rest_framework import serializers

from {{ cookiecutter.project_slug }}.users.models import User as UserType


User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        {%- if cookiecutter.username_type == "email" %}
        fields = ["name", "email"]
        {%- else %}
        fields = ["username", "name"]

        {%- endif %}
