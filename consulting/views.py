from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.utils.translation import ugettext, ugettext_lazy as _
from consulting.models import Topic, Question

import django
if django.VERSION < (1, 3):
    import cbv as class_based_views
else:
    import django.views.generic as class_based_views

def index(request):
    pass
