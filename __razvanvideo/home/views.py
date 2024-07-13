#
#
#
#
#
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect


class HomePageView(TemplateView):
    template_name = 'home/home.html'

class ToateVideoclipurilePageView(TemplateView):
    template_name = 'home/toate-videoclipurile.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     current_filter = self.request.GET.get('filter', '*')
    #     context['current_filter'] = current_filter
    #     return context
