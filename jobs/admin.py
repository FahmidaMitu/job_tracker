from django.contrib import admin
from .models import JobApplication

# Register the JobApplication model to Django Admin
@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('company_name', 'position', 'status', 'application_date', 'deadline')
    
    # Filter options on the right sidebar
    list_filter = ('status', 'application_date')
    
    # Search functionality for company and position
    search_fields = ('company_name', 'position')