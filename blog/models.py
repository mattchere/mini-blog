from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Blogger(models.Model):
    """
    Model representing a blogger.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('blogger-detail', args=[str(self.id)])


class BlogPost(models.Model):
    """
    Model representing one particular blog post by a blogger.
    """
    title = models.CharField(max_length=200)
    post_date = models.DateField()
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        ordering = ["-post_date"]

    def __str__(self):
        """
        String for representing the blog post.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular blog post.
        """
        return reverse('blog-detail', args=[str(self.id)])


class Comment(models.Model):
    """
    Model representing a comment on a blog post.
    """
    commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return (self.text[:75]) if len(self.text) > 75 else self.text

    class Meta:
        ordering = ['post_date']

