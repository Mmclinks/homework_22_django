# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User
#
#
# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ['email', 'username', 'phone_number', 'avatar', 'country', 'is_staff', 'is_active']
#     list_filter = ['is_staff', 'is_active', 'country']
#     search_fields = ['email', 'username', 'phone_number']
#     ordering = ['email']
#
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'avatar', 'country')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )
#
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': (
#                 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'avatar', 'country',
#                 'is_staff')}
#          ),
#     )
#
#
# admin.site.register(User, CustomUserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar', 'phone_number', 'country')}),
    )


admin.site.register(User, CustomUserAdmin)
