from django.contrib import admin

from .models import ImageClickCount, UrlClickCount, ButtonClickCount

admin.site.register(ImageClickCount)
admin.site.register(UrlClickCount)
admin.site.register(ButtonClickCount)
