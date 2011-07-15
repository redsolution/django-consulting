from django.conf.urls.defaults import *


urlpatterns = patterns('consulting.views',
    url(r'^$', 'index', name='faq_index'),
)
