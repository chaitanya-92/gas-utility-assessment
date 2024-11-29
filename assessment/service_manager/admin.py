from django.contrib import admin
from .models import UserProfile, ServiceTicket

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'contact_number']
    search_fields = ['full_name', 'email']

@admin.register(ServiceTicket)
class ServiceTicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['category', 'description']
