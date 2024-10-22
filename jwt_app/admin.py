from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import *

class CustomUserAdmin(BaseUserAdmin):
    # Specify the fields to display in the admin list view
    list_display = ('id', 'email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

    # Define the fieldsets to display on the user edit page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Fields for the "Add user" page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

    # Specify which fields are used for ordering and searching
    ordering = ('email',)
    search_fields = ('email', 'name')

# Register the custom user model and admin interface
admin.site.register(User, CustomUserAdmin)
