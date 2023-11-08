from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model, decorators
from django.contrib.auth import forms as admin_forms
{%- if cookiecutter.username_type == "email" %}
from django.forms import EmailField
{%- endif %}
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        {%- if cookiecutter.username_type == "email" %}
        field_classes = {"email": EmailField}
        {%- endif %}


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        {%- if cookiecutter.username_type == "email" %}
        fields = ("email",)
        field_classes = {"email": EmailField}
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }
        {%- else %}
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }
        {%- endif %}


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        {%- if cookiecutter.username_type == "email" %}
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name",)}),
        {%- else %}
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        {%- endif %}
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["{{cookiecutter.username_type}}", "name", "is_superuser"]
    search_fields = ["name"]
    {%- if cookiecutter.username_type == "email" %}
    ordering = ["id"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    {%- endif %}
