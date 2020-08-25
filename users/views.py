from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import UserRegisterationForm ,UserUpdateform ,ProfileUpdateform

# Create your views here.
def register(request):
    if request.method =="POST":
        form=UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            # print(username)
            messages.success(request,f'Account created for {username} ....')
            return redirect('home')
    else:
        form=UserRegisterationForm()

    return render(request,'users/register.html' ,{'form':form})


# Profile Show
@login_required
def profile(request):
    if request.method =="POST":
        u_form=UserUpdateform(request.POST,instance=request.user)
        p_form=ProfileUpdateform(request.POST,
                                  request.FILES,
                                  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()  
            p_form.save()   
            messages.success(request,f'Your Profile Has been Updated Successfully...')
            return redirect('profile')                     
    else:
        u_form=UserUpdateform(instance=request.user)
        p_form=ProfileUpdateform(instance=request.user.profile)    
    
    context={
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,"users/profile.html" ,context)