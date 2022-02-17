from django.contrib import admin

from home.models import Branch, Contact, Teacher

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'message']
    list_filter = ['name']
    search_fields = ['name__startswith']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'branch']
    list_filter = ['branch']
    search_fields = ['first_name__startswith']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Branch)
admin.site.register(Teacher, TeacherAdmin)
