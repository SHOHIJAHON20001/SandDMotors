from django.db import models

# Create your models here.


class Galareya(models.Model):
    image = models.ImageField(upload_to='Cars')
    name = models.CharField(max_length=255, blank=True, null=True) #Mashina nomi
    model = models.CharField(max_length=255, blank=True, null=True)  #mashina modeli
    slug = models.SlugField() #slug
    gibrid = models.CharField(max_length=255, blank=True, null=True)  # gibrid
    max_speed = models.PositiveBigIntegerField()  #max tezlik
    motor = models.FloatField(null=True)  #motor
    passangers = models.PositiveBigIntegerField() #passajirlar soni
    battery_capacity = models.FloatField()  #barareya hajmi kv
    max_cruising_range = models.PositiveBigIntegerField() #nech km yuradi

    class Meta:
        verbose_name = 'Galareya'
        verbose_name_plural = 'Galareya'
    
    def for_home(self):
        return self.model