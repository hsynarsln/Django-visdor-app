from django.contrib import admin

from home.models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'message']
    list_filter = ['name']
    search_fields = ['name__startswith']


admin.site.register(Contact, ContactAdmin)
