from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length=300)
    image = models.ImageField(upload_to= settings.BLOB_READ_WRITE_TOKEN, null=True, blank=True)  # ImageField should be correctly defined
    description = models.TextField()
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True, auto_now_add=False)
    
    
    def __str__(self):
        return self.title + '\n' + self.description ++ '\n' + self.image
    
     
    
