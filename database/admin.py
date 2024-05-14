from django.contrib import admin

import Songs
from database.models import Playlist, Song, Users

# Register your models here.

admin.site.register(Users)
admin.site.register(Song)
admin.site.register(Playlist)

