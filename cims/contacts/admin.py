from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','asset_id', 'name', 'email', 'message','contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'rollno', 'asset_id')
    list_per_page = 5

admin.site.register(Contact, ContactAdmin)