from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django import forms
from django.contrib.auth.decorators import login_required

from .forms import UserProfileForm
from .models import UserProfile, Interest




# Create your views here.
def register(request):
    #pass
    if request.method == "POST":
        #register_form = UserCreationForm(request.POST)
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New user account created. Login to get started!"))
            return redirect('register')
    else:
        #register_form = UserCreationForm()
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})

@login_required
def userprofile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
                
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            
            # cd = form.cleaned_data
            # assert False
            profile.interests.clear()
            for interest in form.cleaned_data['interests']:
                print(interest)
                created_interest, created = Interest.objects.get_or_create(interest_name=interest)
                print("created:", created_interest)
                
                profile.interests.add(created_interest)
                profile.save()
            messages.success(request, ("Your changes have been saved"))
            #form.save_m2m()

            return redirect('userprofile')
        else:
            print(form.errors)
            #form = ReviewForm(user=request.user)
    else:
        form = UserProfileForm(instance=request.user, 
                initial={
                    #'id': profile.id,
                    'email': profile.email,
                    'age': profile.age,
                    'gender': profile.gender,
                    'education': profile.education,
                    'interests': list(profile.interests.values_list('interest_name', flat=True))
                    #'interests': profile.interests.values_list('interest_name', flat=True)
                })

        print(form.errors)
    
    # query
    current_interests = UserProfile.objects.filter(user=request.user)
    # list
    list_interests = list(profile.interests.values_list('interest_name', flat=True))
    
    #print("List:",list_interests)
    #print("Cur:",current_interests)
    context = {
       'form': form,
       'current_interests': current_interests,
       'list_interests': list_interests
    }
        
    return render(request, 'userprofile.html', context)

