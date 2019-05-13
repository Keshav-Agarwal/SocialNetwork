from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

'''
class Profile(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    posts = models.CharField(max_length=5000)
    pics = models.ImageField()
    friends = ArrayField(
        models.IntegerField(), null=True, blank=True
    )
    dob = models.DateField(default=datetime.today)
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

'''


class Profile(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # posts = models.CharField(max_length=5000)
    # pics = models.ImageField()
    # friends = ArrayField(models.IntegerField(), null=True, blank=True)
    dob = models.DateField(default=datetime.today)
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')

    def __str__(self):
        return self.user.username


class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)


class TextPost(Posts):
    text = models.CharField(max_length=1000)


class ImagePost(Posts):
    description = models.CharField(max_length=1000)
    pic = models.ImageField()


class Friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friend = models.IntegerField()


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
