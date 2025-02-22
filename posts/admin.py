from django.contrib import admin
from . import models



@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate')
    list_filter = ('rate',)
    search_fields = ('title', 'content')
    ordering = ('rate',)


admin.site.register(models.Category)
admin.site.register(models.Tag)
