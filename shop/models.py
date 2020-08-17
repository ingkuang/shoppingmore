from django.db import models
from django.db.models import SlugField
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
            return self.name

        def get_absolute_url(self):
            return reverse('shop:product_in_category', args=[self.slug])

# Create your models here.
