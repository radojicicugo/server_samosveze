from django.contrib import admin

from . models import Contact

# Register your models here.
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['message','name','email']

admin.site.register(Contact, ContactAdmin)