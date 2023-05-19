from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
# This is a model class for a user with fields for first name, last name, username, password, date of
# birth, and profile picture.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField("")
    # date_of_birth = models.DateTimeField("", help_text="Please use the following format: <em>YYYYMMDD</em>.")
    profile_picture = models.CharField(max_length=500)
    def __str__(self):
        return self.username
    

# This is a Django model class for a blog post with fields for author, title, text, blog photo, and
# published date, as well as a method to check if the post was published recently.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    blog_photo = models.CharField(max_length=500)
    published_at = models.DateTimeField("date published")
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.published_at >= timezone.now() - datetime.timedelta(days=1)