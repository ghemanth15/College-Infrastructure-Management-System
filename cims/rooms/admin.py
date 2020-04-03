from django.contrib import admin

from .models import Rooms

class RoomsAdmin(admin.ModelAdmin):
    list_display = ('id','unique_id', 'asset_type', 'asset_no', 'block_no', 'room_no', 'date_of_purchase')
    list_display_links = ( 'id','unique_id')
    list_filter = ('block_no','room_no','asset_type',)
    #list_editable = ('is_published',)
    list_per_page = 25
    search_fields = ('asset_type', 'asset_no', 'room_no', 'block_no','unique_id','date_of_purchase')

admin.site.register(Rooms, RoomsAdmin)