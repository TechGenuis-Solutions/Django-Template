from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from users import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    pass
