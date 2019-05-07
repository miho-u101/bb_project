from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Cruiser

# Create your views here.

class index(TemplateView):
    template_name = 'index.html'    
    def get(self, request, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

class about(TemplateView):
    template_name = 'about.html'    
    def get(self, request, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

class blog(TemplateView):
    template_name = 'blog.html'    
    def get(self, request, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

class contact(TemplateView):
    template_name = 'contact.html'    
    def get(self, request, *args, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)

class portfolio(TemplateView):
    template_name = 'portfolio.html'    
    def get(self, request, *args, **kwargs):
        #context = super(TemplateView, self).get_context_data(**kwargs)
        cruiser_list = Cruiser.objects.all()
        #return render(self.request, self.template_name, context)
        return render(self.request, self.template_name, {'cruiser_list': cruiser_list})

