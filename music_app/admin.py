from django.contrib import admin
from .models import Song,Watchlater,Channel,History
# Register your models here.

admin.site.register(Song)
admin.site.register(Watchlater)
admin.site.register(Channel)
admin.site.register(History)