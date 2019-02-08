from django.contrib import admin


from . models import QueueRecord, MatchRecord, QueueCourt, Court

admin.site.register(QueueRecord)
admin.site.register(MatchRecord)


admin.site.register(QueueCourt)
admin.site.register(Court)
