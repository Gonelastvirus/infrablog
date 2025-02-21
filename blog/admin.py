from django.contrib import admin
from .models import Post,RedHatPost,vmwarepost,Comment
from ckeditor.widgets import CKEditorWidget
from django.db import models

   
class RedHatPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
class vmwarepostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

class PostAdmin(admin.ModelAdmin):
    
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at')
    search_fields = ('name', 'email', 'content')
    list_filter = ('created_at',)
    actions = ['delete_selected'] 


admin.site.register(Post, PostAdmin)
admin.site.register(RedHatPost, RedHatPostAdmin)
admin.site.register(vmwarepost, vmwarepostAdmin)
