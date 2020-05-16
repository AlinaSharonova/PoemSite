from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from basis.forms import CreativeUserForm, CreativeUserChangeForm
from basis.models import User, UserToken

admin.site.register(User)
admin.site.register(UserToken)

class CreativeUserAdmin(UserAdmin):
    add_form = CreativeUserForm
    form = CreativeUserChangeForm
    model = User
    list_display = ['email', 'username', 'info', 'photo']
