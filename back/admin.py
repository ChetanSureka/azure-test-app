from django.contrib import admin
from .models import Categories, Playlists

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'datecreated')
    search_fields = ('id', 'name')
    readonly_fields = ('id', 'datecreated')
    filter_horizontal = ()
    list_filter = ()

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'channelname', 'category', 'url', 'datecreated')
    search_fields = ('id', 'channelname', 'category', 'url')
    readonly_fields = ('id', 'datecreated')
    filter_horizontal = ()
    list_filter = ()
    

admin.site.register(Categories, CategoryAdmin)
admin.site.register(Playlists, PlaylistAdmin)