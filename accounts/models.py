from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
    ('M','M'),
    ('F','F'),
    ('O','Other'),
    ('','Prefer not to say')
)

EDU_CHOICES = (
    ('0','No schooling completed'),
    ('1','Nursery school to 8th grade'),
    ('2','Some high school, no diploma'),
    ('3','High school graduate, diploma or the equivalent'),
    ('4','Some college credit, no degree'),
    ('5','Trade/technical/vocational training'),
    ('6','Associate degree'),
    ('7','Bachelor’s degree'),
    ('8','Master’s degree'),
    ('9','Professional degree'),
    ('10','Doctorate degree'),
    ('','Prefer not to say')
)

INTEREST_CHOICES = (
        ("ELE", "Electronics"),
        ("HYG", "Hygiene"),
        ("SPO", "Sports"),
        ("CLO", "Clothes"),
)

# Create your models here.

class UserProfile(models.Model):
    id = models.BigIntegerField(primary_key = True)
    #user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='profile',default='0')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    email = models.EmailField(null=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(null=True,max_length=2,choices=GENDER_CHOICES)
    education = models.CharField(null=True,max_length=30,choices=EDU_CHOICES)
    
    interests = models.ManyToManyField('Interest',related_name='user_interests',default=None)
    
    def __str__(self):
        return self.user.username

class Interest(models.Model):
    id = models.BigIntegerField(primary_key = True)
    interest_name = models.CharField(max_length=30)

    def __str__(self):
        return self.interest_name
