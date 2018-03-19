# models.py
# File that represents the database model/schema

from django.db import models
from django.core.validators import *

# table that stores all information related to on-campus dormitories 
class Dorm(models.Model):
    created_at = models.DateTimeField('time created', auto_now = True);
    updated_at = models.DateTimeField('time updated', auto_now = True);
    dorm_id = models.AutoField(primary_key=True);
    name = models.CharField(max_length=500);
    address = models.CharField(max_length=500);
    gender_policy = models.CharField(max_length=500);
    bathroom_style = models.CharField(max_length=500);
    room_style = models.CharField(max_length=500);
    amenities = models.CharField(max_length=500);
    class_years = models.CharField(max_length=500);
    comments = models.CharField(max_length=500);
    handicap_access = models.BooleanField();
    custodial_services = models.BooleanField();
    dorm_image = models.ImageField(upload_to='images/', blank=True);
    lat = models.CharField(max_length=50, default=0);
    long = models.CharField(max_length=50, default=0);


# table that stores all information related to user reviews for dorms
# dorm object stored as the foreign key 

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    FLOOR_CHOICES = (
        ('Basement', 'Basement'),
        ('First', 'First'),
        ('Second', 'Second'),
        ('Third', 'Third'),
        ('Fourth', 'Fourth'),
        ('Fifth', 'Fifth'),
    )

    ROOM_CHOICES = (
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Triple', 'Triple'),
        ('Suite', 'Suite'),
    )  

    created_at = models.DateTimeField('time created', auto_now = True);
    updated_at = models.DateTimeField('time updated', auto_now = True);
    rating = models.IntegerField(choices = RATING_CHOICES, default=3);
    handicap_rating = models.IntegerField(choices = RATING_CHOICES, default=3);
    competetiveness = models.IntegerField(choices = RATING_CHOICES, default=3);
    review_id = models.AutoField(primary_key=True);
    user = models.CharField(max_length=150, default=0);
    room_type  = models.CharField(choices = ROOM_CHOICES, default='Single', max_length=10);
    floor = models.CharField(choices = FLOOR_CHOICES, default='First', max_length=10);
    title = models.CharField(max_length=100);
    comment = models.CharField(max_length=500);
    dorm = models.ForeignKey(Dorm, on_delete=models.CASCADE);
    image = models.ImageField(upload_to='uploads/');
