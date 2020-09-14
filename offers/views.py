from django.shortcuts import render
from .models import Offer_electronics_item, Offer_sports_item, Offer_clothes_item, Offer_hygiene_item
from accounts.models import UserProfile

# Create your views here.
def electronics_list(request):
    electronics_items = Offer_electronics_item.objects.all().order_by("product")
    return render(request, 'electronics.html', {'offers_electronics': electronics_items})

#def accept_electronics(request, offer_id):
#    offer = TaskList.objects.get(pk=offer_id)
#    offer.delete()
#    return redirect('electronics_list')

def hygiene_list(request):
    hygiene_items = Offer_hygiene_item.objects.all().order_by("product")
    return render(request, 'hygiene.html', {'offers_hygiene': hygiene_items})

def clothes_list(request):
    clothes_items = Offer_clothes_item.objects.all().order_by("product")
    return render(request, 'clothes.html', {'offers_clothes': clothes_items})

def sports_list(request):
    sports_items = Offer_sports_item.objects.all().order_by("product")
    return render(request, 'sports.html', {'offers_sports': sports_items})


def offer_list(request):
    profile = UserProfile.objects.get(user=request.user)
    list_interests = list(profile.interests.values_list('interest_name', flat=True))
    return render(request, 'offer_list.html', {'list_interests': list_interests})
