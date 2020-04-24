from django.contrib import admin
from .models import *


admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(StandardSubject)
admin.site.register(Chapter)
admin.site.register(ChapterTopic)