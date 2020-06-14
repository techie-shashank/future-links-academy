# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from . import constants as study_constants
from .models import StudyMaterial, ChapterDetail, PreviousYearPapers


class ChapterListView(ListView):
    template_name = 'chapter_list.html'

    def get_queryset(self):
        return ChapterDetail.objects.all().order_by('chapter_no')

    def get_context_data(self, *args, **kwargs):
        context = super(ChapterListView, self).get_context_data(**kwargs)
        context.update({
            'subjects': study_constants.SUBJECT_CHOICES,
            'Standards': study_constants.STANDARD_CHOICES
        })
        return context


class StudyMaterialView(ListView):
    template_name = 'study_material_list.html'
    model = StudyMaterial

    def get_queryset(self):
        chapter_no = self.kwargs.get('pk')
        return StudyMaterial.objects.filter(chapter=chapter_no)


class PreviousYearPaperListView(ListView):
    template_name = 'previous_year_papers.html'

    def get_queryset(self):
        return PreviousYearPapers.objects.all().order_by('-year')

    def get_context_data(self, *args, **kwargs):
        context = super(PreviousYearPaperListView, self).get_context_data(**kwargs)
        context.update({
            'subjects': study_constants.SUBJECT_CHOICES,
            'Standards': study_constants.STANDARD_CHOICES
        })
        return context
