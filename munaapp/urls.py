from django.contrib import admin
from django.urls import path, include

from general import views as general_views
from accounts import views as accounts_views
from offers import views as offers_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('offers/', include('offers.urls')),
    path('contact/', general_views.contact, name='contact'),
    path('about-us/', general_views.about, name='about'),
    path('', general_views.index, name='index'),
]
