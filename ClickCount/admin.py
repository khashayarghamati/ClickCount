from django.contrib import admin

from .models import (ImageClickCount, UrlClickCount,
                     ButtonClickCount, UrlMonitoring)

admin.site.register(ImageClickCount)
admin.site.register(UrlClickCount)
admin.site.register(ButtonClickCount)
admin.site.register(UrlMonitoring)
