from django.contrib import admin

from notes.models import Note

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    
admin.site.register(Note, NotesAdmin)