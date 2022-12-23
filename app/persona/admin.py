from django.contrib import admin

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    search_fields = ['job']
    list_display = ('id','full_name','job','email','phone','created')

admin.site.register(Person, PersonAdmin)
