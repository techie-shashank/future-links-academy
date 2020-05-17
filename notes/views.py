from django.views.generic import DetailView, ListView, TemplateView

from . models import *


class BasePageMixin(object):

    def get_context_data(self, *args, **kwargs):
        context = super(BasePageMixin, self).get_context_data(*args, **kwargs)
        context['standards'] = Standard.objects.all()
        return context


class TopicDetailView(BasePageMixin, DetailView):
    model = ChapterTopic
    template_name = 'notes.html'


class ChapterListView(BasePageMixin, ListView):
    model = Chapter
    template_name = 'chapter_list.html'


class NotesPageView(TemplateView):
    template_name = 'notes_page.html'
