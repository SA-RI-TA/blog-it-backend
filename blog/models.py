from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField("")
    profile_picture = models.CharField(max_length=500)
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    blog_photo = models.CharField(max_length=500)
    published_at = models.DateTimeField("date published")
    def __str__(self):
        return self.title