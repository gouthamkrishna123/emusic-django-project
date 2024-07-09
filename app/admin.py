from django.contrib import admin

from app.models import customer
from app.models import Album
from app.models import music
from app.models import Songs
# Register your models here.

admin.site.register(customer)

admin.site.register(music)
admin.site.register(Album)
admin.site.register(Songs)
