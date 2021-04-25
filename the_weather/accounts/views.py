from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('weather/weather.html')
    return render(request,'login.html',{'form':form})



