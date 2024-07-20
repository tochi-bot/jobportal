
from django.contrib import admin
from .models import Company, Job, Application
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Company)
class CompanyAdmin(SummernoteModelAdmin):

    list_display = ('name', 'location', 'description')
    search_fields = ['name']
    list_filter = ('description',)
    prepopulated_fields = {'location': ('name',)}
    summernote_fields = ('description',)

@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):

    list_display = ('title', 'company', 'location', 'description')
    search_fields = ['title', 'company', 'description']
    list_filter = ('description',)
    prepopulated_fields = {'description': ('title',)}
    summernote_fields = ('description',)

@admin.register(Application)
class ApplicationAdmin(SummernoteModelAdmin):

    list_display = ('user', 'job', 'cover_letter')
    search_fields = ['user']
    list_filter = ('job',)
    prepopulated_fields = {'cover_letter': ('user',)}
    summernote_fields = ('cover_letter',)

