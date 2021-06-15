from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.last_name
