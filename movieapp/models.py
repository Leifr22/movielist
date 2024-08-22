from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class DressingRoom(models.Model):
    floor=models.IntegerField()
    number=models.IntegerField()
    def __str__(self):
        return f'{self.floor} {self.number}'

class Director(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    director_email = models.EmailField()
    def __str__(self):
        return f'{self.name} {self.surname}'
    def get_url(self):
        return reverse('director_list',args=[self.id])

class Actor(models.Model):
    Male='M'
    Female='F'
    GENDER_CHOICE=[
        (Male,'Мужчина'),
        (Female,'Женщина'),
    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender=models.CharField(max_length=100,choices=GENDER_CHOICE, default=Male)
    dressing=models.OneToOneField(DressingRoom,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        if self.gender==self.Male:
            return f'Актер - {self.name} {self.surname}'
        else:
            return f'Актриса - {self.name} {self.surname}'
    def get_url(self):
        return reverse('actors',args=[self.id])

class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles'),
    ]
    name= models.CharField(max_length=40)
    ratings=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    year=models.IntegerField(null=True,blank=True)
    currency=models.CharField(max_length=3, choices=CURRENCY_CHOICES,default=RUB)
    budget=models.IntegerField(default=1000000,blank=True,validators=[MinValueValidator(1)])
    slug=models.SlugField(default='', null=False)
    director=models.ForeignKey(Director, on_delete=models.SET_NULL, null=True,related_name='movies')
    actors=models.ManyToManyField(Actor,related_name='actors')

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Movie,self).save(*args,**kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.ratings}%'
