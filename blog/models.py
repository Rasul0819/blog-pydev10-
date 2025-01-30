from django.db import models


# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=255,)
    post = models.TextField()
    pub_date = models.DateTimeField(
        auto_now=True,auto_created=True
    )
    image = models.ImageField(
        upload_to='media/images/',
        blank=True,null=True)
    