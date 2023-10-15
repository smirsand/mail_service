# Generated by Django 4.2.6 on 2023-10-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='заголовок')),
                ('content', models.TextField(verbose_name='содержимое статьи')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение')),
                ('count_views', models.PositiveIntegerField(default=0, verbose_name='количество просмотров')),
                ('publication_date', models.DateField(auto_now_add=True, verbose_name='дата публикации')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блог',
            },
        ),
    ]
