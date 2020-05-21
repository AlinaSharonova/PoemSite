# Register your models here.
from django.contrib import admin
from .models import Poem, CommentPoem


class PoemAdmin(admin.ModelAdmin):
     list_display = ("id", "title", "author", "category", "owner", "published_date")
     list_display_links = ("title",)
     list_filter = ("category", "author", "owner")
     search_fields = ("title", "author")
     ordering = ('author', 'owner', 'published_date')
     exclude = ('owner',)

     def save_model(self, request, obj, form, change):
         if not obj.pk:
             obj.owner = request.user
         super().save_model(request, obj, form, change)


class CommentPoemAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "id_poem", "created")
    list_display_links = ("id_poem",)
    list_filter = ( "user", "id_poem")
    search_fields = ("id_poem", "user")
    ordering = ('user', 'id_poem', 'created')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Poem, PoemAdmin)
admin.site.register(CommentPoem, CommentPoemAdmin)