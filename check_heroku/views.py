from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Post


class Home(ListView):
    model = Post
    template_name = 'check_heroku/index.html'
    context_object_name = 'posts'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     #context['title'] = 'Classic Blog Design'
    #     return context
    

# def index(request):
#     return HttpResponse('Hello world')
