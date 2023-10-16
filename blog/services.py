from django.conf import settings
from django.core.cache import cache


def get_blog_cache(self):
    if settings.CACHE_ENABLED:
        key = 'blog_list'
        queryset_blog_list = cache.get(key)
        if queryset_blog_list is None:
            queryset_blog_list = self.object_list.all()
            cache.set(key, queryset_blog_list)
    else:
        queryset_blog_list = self.object_list.all()

    return queryset_blog_list