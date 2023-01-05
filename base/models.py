from django.db import models
from django.contrib.auth.models import User

# Topic model
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Room model
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    



# Message model
class Message(models.Model):
    # One-to-many relationship, need a foreign key
    # (user can have multiple messages, as can a room)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Only want the first 50 characters
        return self.body[0:50]