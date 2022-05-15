import uuid
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100, blank=True,null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    Id = models.IntegerField(unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.name)

class Books(models.Model):
    
    title = models.CharField(max_length=100, blank=True,null=True)
    description = models.TextField(max_length=100, blank=True,null=True)
    rating = models.DecimalField(decimal_places=1, max_digits=20, default=0.0)
    
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    Id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.title)
    