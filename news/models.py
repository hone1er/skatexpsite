from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    preview = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    
