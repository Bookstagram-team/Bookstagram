from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class User(AbstractUser):
    is_customer = models.BooleanField('Is reader', default=False)
    is_employee = models.BooleanField('Is author', default=False)

#tambahan untuk attirbut tiap user itu apa aja
class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
	name = models.CharField(max_length=30, blank=True, null=True)
	bio = models.TextField(max_length=500, blank=True, null=True)
	# birth_date=models.DateField(null=True, blank=True)
	# location = models.CharField(max_length=100, blank=True, null=True)
	picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)
	# followers = models.ManyToManyField(User, blank=True, related_name='followers')

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

class Post(models.Model):
	title = models.TextField()
	body = models.TextField()
	created_on = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
	name = models.CharField(max_length=255)
	date_added = models.DateField(auto_now_add=True)
	rate = models.IntegerField()
	comments = models.TextField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class Reply(models.Model):
    post = models.ForeignKey('main.Post', on_delete=models.CASCADE)  
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Reply by {self.author.username} on {self.created_date}'
