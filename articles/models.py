from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.


class Article(models.Model):
    """Article Model"""

    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")

    def __str__(self):
        """string method"""
        return self.title

    def get_absolute_url(self):
        """Get the absolute url for the model"""
        return reverse("article_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    """Comment Model"""

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")

    text = models.CharField(max_length=140)

    def __str__(self):
        """string method"""
        return self.text

    def get_absolute_url(self):
        """get the absolute url for the comment"""

        # would be better to have an actual detail view for the comment
        return reverse("article_list")
