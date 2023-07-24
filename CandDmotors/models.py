from django.db import models

# Create your models here.


class Galareya(models.Model):
    image = models.ImageField(upload_to='Cars')
    name = models.CharField(max_length=255, blank=True, null=True) #Mashina nomi
    model = models.CharField(max_length=255, blank=True, null=True)  #mashina modeli
    slug = models.SlugField() #slug
    gibrid = models.CharField(max_length=255, blank=True, null=True)  # gibrid
    max_speed = models.PositiveBigIntegerField(blank=True, null=True)  #max tezlik
    motor = models.FloatField(blank=True, null=True)  #motor
    passangers = models.PositiveBigIntegerField(blank=True, null=True) #passajirlar soni
    battery_capacity = models.FloatField(blank=True, null=True)  #barareya hajmi kv
    max_cruising_range = models.PositiveBigIntegerField(blank=True, null=True) #nech km yuradi

    class Meta:
        verbose_name = 'Galareya'
        verbose_name_plural = 'Galareya'
    
    
    def for_contact(self):
        return f"{self.name} {self.model}"