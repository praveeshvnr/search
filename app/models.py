from django.db import models

# Create your models here.
class Profile_card(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    images = models.ImageField(default = "default.png", upload_to="images")
    phone=models.CharField( max_length=255, default="00")
    place=models.CharField(max_length=255,  default="non")