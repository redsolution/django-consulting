from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import datetime


class Role(models.Model):
    user = models.ForeignKey('auth.User', related_name='faq_roles')
    name = models.CharField(verbose_name=_('Role name'), max_length=100)

    def __unicode__(self):
        return unicode(self.name)

class TopicManager(models.Manager):

    def published(self):
        return self.get_query_set().filter(hidden=False)

class Topic(models.Model):
    roles = models.ManyToManyField('Role', verbose_name=_('Topic experts'))
    name = models.CharField(verbose_name=_('Consultation topic'), max_length=100)
    slug = models.SlugField(verbose_name=_('Topic relative URL'), max_length=100)
    hidden = models.BooleanField(verbose_name=_('Hide topic from public view'), default=False)

    objects = TopicManager()

    def __unicode__(self):
        return unicode(self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('consulting_topic', [str(self.slug)])

    @property
    def broadcast(self):
        '''
        If topic has no experts, it will broadcast questions to all experts
        '''
        return self.roles.all().count() > 0

class QuestionManager(models.Manager):

    def pblished(self):
        return self.get_query_set().filter(date_answered__isnull=False, hidden=False)

class Question(models.Model):
    date_added = models.DateTimeField(verbose_name=_('Date question asked'), auto_now_add=True)
    date_answered = models.DateTimeField(verbose_name=_('Date question answered'), null=True)
    text = models.TextField(verbose_name=_('Question text'))
    answer = models.TextField(verbose_name=_('expert answer'))
    hidden = models.BooleanField(verbose_name=_('Hide question from public view'), default=False)
    topic = models.ForeignKey('Topic', verbose_name=_('Question topic'))
    # question callback info
    username = models.CharField(verbose_name=_('Username'),
        help_text=_('Username will be shown on site when your question will be answered'),
        max_length=50)
    email = models.EmailField(verbose_name=_('Email'),
        help_text=_('Your email can be used for personal correspondence with expert. It will not be published'),
        null=True, blank=True)
    comment = models.CharField(
        verbose_name=_('Comment for expert, not will be published'),
        max_length=100, null=True, blank=True)
    expert = models.ForeignKey('auth.User',
        verbose_name=_('Expert who answered the question'), null=True, blank=True)

    def __unicode__(self):
        return unicode(self.text)

    @models.permalink
    def get_absolute_url(self):
        return ('consulting_question', [str(self.topic.slug), str(self.id)])

    @property
    def answered(self):
        return self.date_answered is not None

    def save(self, *args, **kwds):
        if self.answer:
            self.date_answered = datetime.now()

        super(Question, self).save(*args, **kwds)
