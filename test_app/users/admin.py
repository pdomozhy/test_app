from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group


from .models import User


class UserAdmin(DjangoUserAdmin):

    fieldsets = (
        (None, {
        	'fields': ('app_id', 'username', 'email', 'password')}
        ),
        ('Personal info', {
        	'fields': ('first_name', 'last_name')}
        ),
        ('Custom fields', {
        	'fields': ('is_confirmed', 'role',)}
        ),
        ('Permissions', {
        	'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        ('Important dates', {
        	'fields': ('last_login', 'date_joined',)}
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('app_id',)
    list_display = ('username', 'app_id', 'first_name', 'last_name',
                                'is_confirmed')
    search_fields = ('username', 'email', 'app_id', 'first_name', 'last_name')
    ordering = ('date_joined',)
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'is_confirmed',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
