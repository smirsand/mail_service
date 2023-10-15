from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogListView(ListView):
    """
    Контроллер для просмотра блога.
    """
    model = Blog
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    extra_context = {
        'title': 'Блог'
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()

        return self.object
