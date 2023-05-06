from django.db import models
from django.contrib.auth.models import User
from .Validations import *

# Create your models here.
class RegistrationModel(models.Model):
    profile=models.FileField(upload_to='profileimages/',validators=[validation_for_profile])
    address=models.TextField(blank=False,null=False,validators=[validation_for_address])
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

class PostModel(models.Model):
    # Title=models.TextField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    ak=models.TextField(null=True,blank=True)
    anubhav_gupta=models.CharField(max_length=20,null=True,blank=True)

class PostImagesModel(models.Model):
    images=models.FileField(upload_to='post_images/')
    post_id=models.ForeignKey(PostModel,on_delete=models.CASCADE)

class CommentModel(models.Model):
    comment=models.TextField()
    from_post=models.ForeignKey(PostModel,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',null=True,on_delete=models.CASCADE,related_name='ak')
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)

class likedModel(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    comment_id=models.ForeignKey(CommentModel,on_delete=models.CASCADE)

class ReportedbyPostModel(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    post_id=models.ForeignKey(PostModel,on_delete=models.CASCADE)

class ReportedbyCommentModel(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    comment_id=models.ForeignKey(CommentModel,on_delete=models.CASCADE)