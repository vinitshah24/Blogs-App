from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # One-One relatioship with User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Upload to --> directory where it will be saved
    # Need Pillow library for working with images
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'Profile: {self.user.username}'

    # Overriding a method to make changes when save() is called
    # Resizing the image to smaller size for effeciency [Using Pillow]
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            new_size = (300, 300)
            img.thumbnail(new_size)
            img.save(self.image.path)
