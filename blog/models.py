from django.db import models
from django.urls import reverse

# Create your models here.
class Topic(models.Model):
    topic = models.CharField(max_length=200)

    def __str__(self):
        return self.topic

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )
    body = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, default=1)
    date = models.DateField(auto_now_add=True, )
    image = models.ImageField(null=True, blank=True, upload_to="blog/")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

class Image(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, default=1)
    date = models.DateField(auto_now_add=True, )
    image1 = models.ImageField(null=True, blank=True, upload_to="images/")
    image2 = models.ImageField(null=True, blank=True, upload_to="images/")
    image3 = models.ImageField(null=True, blank=True, upload_to="images/")
    image4 = models.ImageField(null=True, blank=True, upload_to="images/")
    image5 = models.ImageField(null=True, blank=True, upload_to="images/")
    image6 = models.ImageField(null=True, blank=True, upload_to="images/")
    image7 = models.ImageField(null=True, blank=True, upload_to="images/")
    image8 = models.ImageField(null=True, blank=True, upload_to="images/")
    image9 = models.ImageField(null=True, blank=True, upload_to="images/")


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

