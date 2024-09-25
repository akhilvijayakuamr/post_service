from django.db import models
from django.utils import timezone
from .storage import S3ImageStorage

# Create your models here.


# Post model

class Post(models.Model):
    user_id = models.IntegerField()
    title = models.TextField(null=False, blank=False)
    post_image = models.ImageField(storage=S3ImageStorage(),upload_to='post_images/')
    content = models.TextField(null=False, blank=False)
    link = models.CharField(null=False, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    is_delete = models.BooleanField(default=False)
    
    
# Post Like
class Like(models.Model):
    user = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_delete = models.BooleanField(default=False)
    

# Post Comment models 
    
class Comment(models.Model):
    user = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_delete = models.BooleanField(default=False)
    
    
    
# Post comment replay

class Reply(models.Model):
    user = models.IntegerField()
    mention_user = models.IntegerField()
    mention_user_full_name = models.CharField(max_length=150)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_delete = models.BooleanField(default=False)
    
    


        