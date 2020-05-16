# Register your models here.
from django.contrib import admin
from .models import Poem, CommentPoem, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'date_of_birth']

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


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Poem, PoemAdmin)
admin.site.register(CommentPoem, CommentPoemAdmin)