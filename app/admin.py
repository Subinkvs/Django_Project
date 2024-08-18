from django.contrib import admin
from .models import CustomUser
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active','phonenumber')
    readonly_fields = ('username', 'email', 'phonenumber','first_name','last_name') 

admin.site.register(CustomUser)
