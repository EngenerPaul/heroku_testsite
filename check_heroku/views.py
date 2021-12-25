from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.db.models import F
from django.urls import reverse_lazy
from django.core.cache import cache

from .models import Post, Tag, Category
from .forms import NewComment


class Home(ListView):
    model = Post
    template_name = 'check_heroku/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'

        context['popular_post'] = cache.get('popular_post')
        if not context['popular_post']:
            context['popular_post'] = Post.objects.order_by('-views')[0]
            cache.set('popular_post', context['popular_post'], 60*30)
        
        return context
    

class PostsByCategory(ListView):
    template_name = 'check_heroku/category.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class PostByTag(ListView):
    template_name = 'check_heroku/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Posts by tag' + str(Tag.objects.get(slug=self.kwargs['slug']))
        return context

class GetPost(DetailView, FormMixin):
    model = Post
    template_name = 'check_heroku/single.html'
    context_object_name = 'post'

    form_class = NewComment

    # needed for writing form post
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # needed for save form
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.save()
        return super().form_valid(form)
    
    # needed for updating page after save form
    def get_success_url(self, **kwargs):
        return reverse_lazy('post', kwargs={'slug':self.get_object().slug})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        context['comments'] = self.object.comments.all() # print comments
        return context

class Search(ListView):
    template_name = 'check_heroku/search.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context