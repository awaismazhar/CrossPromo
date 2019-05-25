from django.db import models

# Create your models here.
class AdvertismentInfo(models.Model):
    GameTitle=models.CharField(max_length=100)
    GameUrl=models.CharField(max_length=1000)
    ImageUrl=models.CharField(max_length=1000)
    # GamePlatform_Choices = (('Android', 'Android'), ('iOS', 'iOS'),)
    # GameOrientation_Choices = (('Landscape', 'Landscape'), ('Potrait', 'Potrait'),)

    # GamePlatform = models.CharField(choices=GamePlatform_Choices, max_length=20)
    # GameOrientation = models.CharField(choices=GameOrientation_Choices, max_length=20)
    AdImage=models.ImageField(upload_to='images/')

  

    def __str__(self):
        return self.GameTitle