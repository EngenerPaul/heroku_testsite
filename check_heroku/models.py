from django.db import models
from django.db.models.base import Model
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='was created')
    
    def __str__(self):
        return self.title
    
    def get_ansolute_url(self):
        return reverse('post', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['title', ]
