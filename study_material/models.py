from __future__ import unicode_literals

from django.db import models

from . import constants


class ChapterDetail(models.Model):

    subject = models.PositiveSmallIntegerField(choices=constants.SUBJECT_CHOICES)
    standard = models.PositiveSmallIntegerField(choices=constants.STANDARD_CHOICES)
    chapter_no = models.PositiveSmallIntegerField()
    chapter_name = models.CharField(max_length=128)

    class Meta(object):
        unique_together = ('subject', 'standard', 'chapter_no',)

    def __str__(self):
        return 'standard: {} - Subject: {} - Chapter: {}'.format(
            self.standard, constants.SUBJECT_CHOICES[self.subject][1], self.chapter_no
        )


class StudyMaterial(models.Model):

    video_link = models.CharField(max_length=1024)
    notes = models.FileField(upload_to=constants.STUDY_MATERIAL_UPLOAD_DIR, max_length=512)
    topic_name = models.CharField(max_length=1024)
    topic_description = models.TextField()
    chapter = models.ForeignKey(ChapterDetail)

    class Meta(object):
        unique_together = ('chapter', 'topic_name',)

    def __str__(self):
        return 'Chapter: {} - Topic: {}'.format(self.chapter, self.topic_name)
