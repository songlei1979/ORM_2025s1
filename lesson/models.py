import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    snippet = models.CharField(max_length=255, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.title

    def published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)


