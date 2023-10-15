from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое статьи')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', blank=True, null=True)
    count_views = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')
    publication_date = models.DateField(auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return f'{self.publication_date} - {self.title}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блог'
