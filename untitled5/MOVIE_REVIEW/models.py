from django.db import models
import datetime
from django.core.urlresolvers import reverse

# Create your models here.
class directors(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=7,blank=True)
    dob = models.DateField(default="2000-01-01")
    description = models.CharField(max_length=2500, blank=True, default='')
    pic = models.URLField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLV4iTgBnY8EbNX9fIe7ijBCwyTKLTZW-NNLjUbiPiNmyxhd-fXw')
    def __str__(self):
        return self.name

class actors(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=7)
    dob = models.DateField(default="2000-01-01")
    description=models.CharField(max_length=2500,blank=True,default='')
    pic = models.URLField(max_length=500, blank=True,default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLV4iTgBnY8EbNX9fIe7ijBCwyTKLTZW-NNLjUbiPiNmyxhd-fXw')
    def __str__(self):
        return self.name

class movies(models.Model):
    title = models.CharField(max_length=100)
    year = models.DateField()
    imdb = models.FloatField(default=10)
    lang = models.CharField(max_length=100)
    director = models.ForeignKey(directors,on_delete=models.CASCADE)
    description = models.CharField(max_length=2500,blank=True,default='')
    trailer=models.URLField(max_length=500, blank=True,default='/')
    userrating = models.FloatField(default=0)
    pic = models.URLField(max_length=500, blank=True,default='http://icons.iconarchive.com/icons/guillendesign/variations-3/256/Default-Icon-icon.png')
    def __str__(self):
        return self.title

class movie_cast(models.Model):
    actor = models.ForeignKey(actors,on_delete=models.CASCADE)
    movie = models.ForeignKey(movies,on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    def __str__(self):
        template = '{0.movie} {0.actor} {0.role}'
        return template.format(self)


class rating(models.Model):
    movie = models.ForeignKey(movies,on_delete=models.CASCADE)
    stars = models.IntegerField()
    pic = models.URLField(max_length=500, blank=True, default='http://icons.iconarchive.com/icons/guillendesign/variations-3/256/Default-Icon-icon.png')
    def __str__(self):
        template = '{0.movie}'
        return template.format(self)

class comments(models.Model):
    class Meta:
        unique_together = ("mov_id", "email")
    comment = models.CharField(max_length=2500, blank=True, default='')
    points = models.IntegerField()
    mov_id = models.ForeignKey(movies, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, blank=False, default='')
    created = models.DateTimeField(auto_now_add=True, blank=True, editable=False)
