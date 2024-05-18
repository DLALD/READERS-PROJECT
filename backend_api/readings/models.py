from django.db import models

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    genre = models.CharField(max_length=100, blank=True)
    published_year = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    pages = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    cover_image_url = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
