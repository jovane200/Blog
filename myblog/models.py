from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager
from cloudinary.models import CloudinaryField


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
        )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    tags = TaggableManager() # to use tags for posts
    image = CloudinaryField('image', blank=True, null=True)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields = ['-publish']),
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):

        return reverse('myblog:post_detail',
                       args=[self.id, self.slug])
    
    def save(self,*args,**kwargs):

        if not self.slug:
            self.slug = slugify(self.title)
        
        super().save(*args,**kwargs)




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)  # Optional: comment moderation

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'