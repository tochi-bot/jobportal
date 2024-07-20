from django.contrib import admin
from .models import BlogPost
from django_summernote.admin import SummernoteModelAdmin

@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'approved')
    search_fields = ['title']
    list_filter = ('content',)
    prepopulated_fields = {'content': ('title',)}
    summernote_fields = ('content',)


