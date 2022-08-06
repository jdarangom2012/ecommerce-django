from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Accounts

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'firts_name', 'last_name', 'user_name', 'last_login', 'date_joined','is_active')
    list_display_link = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',) #Ordena descendentemnet

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Accounts, AccountAdmin)

