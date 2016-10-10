from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from . import models


class UserSettingInline(admin.TabularInline):
    model = models.UserSetting
    extra = 1


class AddressInline(admin.TabularInline):
    model = models.Address
    extra = 1


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    inlines = (UserSettingInline, AddressInline)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'full_name', 'roles')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('date_joined', 'confirmed_email_at')}),
        (_('Login info'), {'fields': ('last_login', 'last_login_ip', 'current_login_ip', 'login_count')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'full_name', 'is_staff', 'is_active', 'role_names')
    list_display_links = ('email', 'full_name', 'role_names')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'roles')
    search_fields = ('email', 'full_name')
    ordering = ('email',)

    def role_names(self, user):
        roles = user.roles.filter(is_active=True)
        if not roles:
            return '-'
        suffix = ''
        if len(roles) > 3:
            suffix = ', … and %i more…' % (len(roles) - 3)
            roles = roles[:3]
        return ', '.join(g.name for g in roles) + suffix


@admin.register(models.Setting)
class SettingAdmin(admin.ModelAdmin):
    model = models.Setting

    list_display = ('name', 'description', 'data_type', 'default')
    list_filter = ('data_type',)
    search_fields = ('name', 'description')


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    model = models.Role

    list_display = ('name', 'description', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
