from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.safestring import mark_safe
from markdown_deux import markdown


class Post(models.Model):
    author          = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title           = models.CharField(max_length=120)
    content         = models.TextField()
    published_date  = models.DateTimeField(auto_now=True)
    draft           = models.BooleanField(default=True)
    slug            = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug': self.slug})

    def get_html(self):
        content = self.content
        html_text = markdown(content)
        return mark_safe(html_text)

    class Meta:
        ordering = ['title']
