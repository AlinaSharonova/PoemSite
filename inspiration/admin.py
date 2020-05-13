# Register your models here.
from django.contrib import admin
from .models import Poem, CommentPoem


class PoemAdmin(admin.ModelAdmin):
     list_display = ("id", "title", "author", "category", "owner", "published_date")
     list_display_links = ("title",)
     list_filter = ("category", "author", "owner")
     search_fields = ("title", "author")
     ordering = ('author', 'owner', 'published_date')
     #readonly_fields = ("owner",)


class CommentPoemAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title_poem", "created")
    list_display_links = ("title_poem",)
   #readonly_fields = ("user",)


admin.site.register(Poem, PoemAdmin)
admin.site.register(CommentPoem, CommentPoemAdmin)