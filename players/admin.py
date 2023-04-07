from django.contrib import admin
from .models import Player, Club



@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    pass
