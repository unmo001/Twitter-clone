from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class TopPageView(TemplateView):
    template_name = 'TopPage.html'


toppageview = TopPageView.as_view()
