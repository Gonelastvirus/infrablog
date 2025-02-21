from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



# Post model to represent each blog post
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()  # Supports image uploads and code blocks
    author = models.CharField(max_length=100, default="Admin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class RedHatPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()  # Supports image uploads and code blocks
    author = models.CharField(max_length=100, default="Admin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class vmwarepost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()  # Supports image uploads and code blocks
    author = models.CharField(max_length=100, default="Admin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    redhat_post = models.ForeignKey('RedHatPost', on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    vmware_post = models.ForeignKey('vmwarepost', on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'