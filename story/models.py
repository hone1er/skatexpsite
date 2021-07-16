from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    content = RichTextField(blank=True, null=True)    
    image = models.ImageField(upload_to='images', blank=True)
    image_alt = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
