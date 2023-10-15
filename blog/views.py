from django.views.generic import ListView, DetailView

from blog.models import Blog
from blog.services import get_blog_cache


class BlogListView(ListView):
    """
    Контроллер для просмотра блога.
    """
    model = Blog
    template_name = 'blog/blog_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        get_blog_cache(self)
        context_data['blog'] = get_blog_cache(self)
        return context_data


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
