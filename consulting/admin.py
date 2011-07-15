from django.contrib import admin
from consulting.models import Topic, Question, Role
from django.utils.translation import ugettext, ugettext_lazy as _


class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'hidden', 'questions')

    def questions(self, instance):
        return instance.questions.all().count()
    questions.short_description = _('Total questions count')

admin.site.register(Topic, TopicAdmin)

admin.site.register(Question)
admin.site.register(Role)
