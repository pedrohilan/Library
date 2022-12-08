from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    numberPages = models.IntegerField(null=False, blank=False)
    lastPageRead = models.IntegerField(null=False, blank=False)
    img = models.ImageField(upload_to='librarymanager/img', default='', null=False, blank=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name