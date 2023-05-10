from django.contrib import admin

from . models import Contact1

# Register your models here.
# Register your models here.
class Contact1Admin(admin.ModelAdmin):
    list_display=['message','name','email',]

admin.site.register(Contact1, Contact1Admin)