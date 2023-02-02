from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Content(models.Model):
    title = models.CharField(max_length=200, verbose_name='Content')
    slug = models.SlugField(null=True, max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True,)
    photo = models.ImageField(upload_to='photos/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Content'

    def get_absolute_url(self):
        return reverse('show_thread', kwargs={'thread_id': self.slug})

    def get_absolute_url_edit(self):
        return reverse('edit_page', kwargs={'thread_id': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cats_id': self.pk})


class Comments(models.Model):
    post = models.ForeignKey('Content', on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    user_comment = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user_comment

