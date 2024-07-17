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

class PortofoliuNuntaPageView(TemplateView):
    template_name = 'home/portofoliu-nunta-Constanta.html'

class PortofoliuBotezPageView(TemplateView):
    template_name = 'home/portofoliu-botez.html'

class PortofoliuAlteEvenimentePageView(TemplateView):
    template_name = 'home/portofoliu-alte-evenimente-Constanta.html'

class DespreMinePageView(TemplateView):
    template_name = 'home/despre-mine.html'

class ContactPageView(TemplateView):
    template_name = 'home/contact.html'

    