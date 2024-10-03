from django.db import models
from music_owner.models import Musician
# Create your models here.
class Album(models.Model):
    Album_name = models.CharField(max_length=50)
    Album_release_date = models.DateField()
    CHOICES = [('1',1),('2',2),('3',3),('4',4),('5',5)]
    Ratings = models.CharField(
        max_length=10, 
        choices=CHOICES, 
        default='3'  # Default to 'Good'
    )
    Author = models.ForeignKey(Musician,on_delete=models.CASCADE)
    def __str__(self):
        return self.Album_name
    