from django.contrib import admin

from .models import Person, Reunion, Hobby


class PersonAdmin(admin.ModelAdmin):
    search_fields = ['job']
    list_display = ('id','full_name','job','email','phone','created')


class HobbyAdmin(admin.ModelAdmin):
    search_fields = ['hobby']
    list_display = ('id','hobby')


class ReunionAdmin(admin.ModelAdmin):
    search_fields = ['fecha']
    list_display = ('id','person','fecha','hora','asunto')

admin.site.register(Person, PersonAdmin)
admin.site.register(Hobby, HobbyAdmin)
admin.site.register(Reunion, ReunionAdmin)
