from django.contrib import admin
from .models import Bb, Rubric

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'auther', 'genre', 'status', 'data', 'give_out', 'give_in')
    list_display_links = ('title', 'auther', 'genre')
    search_fields = ('title', 'auther', 'genre',)


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)

