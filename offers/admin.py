from django.contrib import admin
from .models import Offer_electronics_item, Offer_clothes_item, Offer_hygiene_item, Offer_sports_item

# Register your models here.
admin.site.register(Offer_electronics_item)
admin.site.register(Offer_clothes_item)
admin.site.register(Offer_hygiene_item)
admin.site.register(Offer_sports_item)