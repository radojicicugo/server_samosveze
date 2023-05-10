from django.contrib import admin

from . models import Podaci

# Register your models here.
# Register your models here.
class PodaciAdmin(admin.ModelAdmin):
    list_display=['image','name','email','description','klass','price','phone','product']

admin.site.register(Podaci, PodaciAdmin)