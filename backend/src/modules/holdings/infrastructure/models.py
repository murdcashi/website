from django.db import models

class Page(models.Model):
    slug = models.SlugField(unique=True)          # e.g. "about", "mission"
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["slug", "is_published"])]

    def __str__(self) -> str:
        return f"{self.slug} - {self.title}"
