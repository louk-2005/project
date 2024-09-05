from django.contrib import admin

from .models import Subscription, MyFavorite

admin.site.register(Subscription)
@admin.register(MyFavorite)
class FavoriteAdmin(admin.ModelAdmin):
    raw_id_fields = ('user','post' )