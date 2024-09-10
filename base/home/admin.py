from django.contrib import admin
from mptt.admin import MPTTModelAdmin,DraggableMPTTAdmin

from .models import Topic, Post, LikePost, DislikePost, Comment

class TopicAdmin(DraggableMPTTAdmin):
    raw_id_fields = ('parent', )
admin.site.register(Topic, TopicAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('issue','topic','slug','primary')
    list_filter = ('updated','topic')
    search_fields = ('body','slug')
    prepopulated_fields = {'slug': ('body',)}
    raw_id_fields = ('topic',)

admin.site.register(Post,PostAdmin)

admin.site.register(LikePost)

admin.site.register(DislikePost)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','post','is_reply','body','created')
    raw_id_fields = ('user','post','reply')