from django.db import models


class Standard(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return '{name}'.format(name=self.name)


class Subject(models.Model):

    name = models.CharField(max_length=128)

    def __str__(self):
        return '{name}'.format(name=self.name)


class StandardSubject(models.Model):

    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return '{std}: {sub}'.format(std=self.standard.name, sub=self.subject.name)


class Chapter(models.Model):

    name = models.CharField(max_length=1024)
    std_subject = models.ForeignKey(StandardSubject, on_delete=models.CASCADE)
    chapter_no = models.PositiveIntegerField()

    def __str__(self):
        return '{name}'.format(name=self.name)


class ChapterTopic(models.Model):

    name = models.CharField(max_length=1024)
    topic_no = models.PositiveIntegerField()
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    detail = models.TextField()

    def __str__(self):
        return '{chapter}: {name}'.format(chapter=self.chapter, name=self.name)

