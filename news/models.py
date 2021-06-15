from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    preview = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True)
    content = RichTextField(blank=True, null=True)    
    image = models.ImageField(upload_to='images', blank=True)
    image_alt = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    

class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" +  self.email