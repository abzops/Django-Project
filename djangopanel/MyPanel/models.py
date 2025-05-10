from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Sale(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=now)  # Add default value for the date field

    def __str__(self):
        return self.product_name

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.project_name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default.png')

    def __str__(self):
        return self.user.username

# Signal to create or update Profile when User is created or saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()