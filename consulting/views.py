from consulting.forms import AskQuestionForm
from consulting.models import Topic, Question
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.generic import list_detail, create_update


def index(request):
    queryset = Topic.objects.published()
    return list_detail.object_list(request, queryset)

def topic(request, slug):

    topic = get_object_or_404(Topic, slug=slug)
    # Form workaround
    form = AskQuestionForm(initial={'topic': topic})
    if request.method == 'POST':
        form = AskQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(topic.get_absolute_url())
    else:
        form = AskQuestionForm(instance=Question(topic=topic))
    extra_context = {'form': form}

    return list_detail.object_detail(request, Topic.objects.published(),
        slug=slug, extra_context=extra_context)

def question(request, slug, object_id):
    return list_detail.object_detail(request, Question.objects.published(), object_id)
