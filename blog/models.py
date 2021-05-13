from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# A model is a class that subclasses django.db.model.models.Model, in which each attribute represents a database field.
# Django will create a table for each model defined in the models.py
# We will define a Post model.


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)  # post title. CharField translate into a VARCHAR column in the SQL db
    slug = models.SlugField(max_length=250,  # field intended to be used in URLs. A slug is a short label that contain
                            unique_for_date='publish')  # only letters, numbers, underscores, or hyphens
    author = models.ForeignKey(User,  # this field is a foreign key which define a many to one relationship
                               on_delete=models.CASCADE,  # Cascade specify that when a referenced user is deleted,
                               related_name='blog_posts')  # the database will also delete it's related blog posts.
    body = models.TextField()  # The body of the post, Translate into a TEXT column in the SQL database
    publish = models.DateTimeField(default=timezone.now)  # indicates when the post was published
    created = models.DateTimeField(auto_now_add=True)  # here, the date will be saved automatically when creating an
    # object
    updated = models.DateTimeField(auto_now=True)  # here, the date will be updated automatically when saving an object
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')  # show the status of a post by using the choices parameter

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
