from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import DemoForm


class DemoView(FormView):
    template_name = 'btn_translation_issue/form.html'
    form_class = DemoForm

    def form_valid(self, form):
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
