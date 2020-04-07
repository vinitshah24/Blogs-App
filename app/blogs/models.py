from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Upon creation of blog, send the reverse url to redirect to post details page
    # reverse() - finding the URL of a given resource
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
