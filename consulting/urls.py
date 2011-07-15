from django.conf.urls.defaults import *

urlpatterns = patterns('consulting.views',
    url(r'^$', 'index', name='consulting_index'),
    url(r'^(?P<slug>[\w-]+)/$', 'topic', name='consulting_topic'),
    url(r'^(?P<slug>[\w-]+)/#question_(?P<object_id>\d{1,4})$', 'question', name='consulting_question'),
)
