from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models


# Create your models here.
class Offer_electronics_item(models.Model):
    brand = models.CharField(max_length=64)
    product = models.CharField(max_length=64)
    product_model = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.product+", "+self.code

    def short_description(self):
        return self.description[:50]+"..."



class Offer_hygiene_item(models.Model):
    brand = models.CharField(max_length=64)
    product = models.CharField(max_length=64)
    product_type = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.product+", "+self.code

    def short_description(self):
        return self.description[:50]+"..."


class Offer_clothes_item(models.Model):
    brand = models.CharField(max_length=64)
    product = models.CharField(max_length=64)
    product_model = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.product+", "+self.code

    def short_description(self):
        return self.description[:50]+"..."


class Offer_sports_item(models.Model):
    brand = models.CharField(max_length=64)
    product = models.CharField(max_length=64)
    product_model = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.product+", "+self.code

    def short_description(self):
        return self.description[:50]+"..."







#class Offer_electronics_item(models.Model):
#    brand = models.CharField(max_length=64)
#    product = models.CharField(max_length=64)
#    product_model = models.CharField(max_length=64)
#    code = models.CharField(max_length=64)
#    description = models.TextField()
#    def __str__(self):
#        return self.product+", "+self.code
#    def short_description(self):
#        return self.description[:50]+"..."
#class User_Electronics_OfferList(models.Model):
#   user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE, related_name='user_el_offer',default=None)
#   #user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
#    offers = models.ManyToManyField('Offer_electronics_item',related_name='user_el_offers',default=None)
#    def __str__(self):
#       return self.user
