from __future__ import unicode_literals

from django.contrib import admin

from.models import StudyMaterial, ChapterDetail, PreviousYearPapers


class StudyMaterialAdmin(admin.ModelAdmin):
    raw_id_fields = ('chapter',)


admin.site.register(StudyMaterial, StudyMaterialAdmin)
admin.site.register(ChapterDetail, admin.ModelAdmin)
admin.site.register(PreviousYearPapers, admin.ModelAdmin)
