from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from product.models import Cart, Item

'''view to load home page with showing added items and
   cart count(if login and item is available in cart) '''
def index(request):
    if request.method=='GET':
        items=Item.objects.all()
        userCart=Cart.objects.filter(user=request.user.id)
        for item in items:
            for cart_item in userCart:
                if item.id == cart_item.item.id:
                    item.cart_added_quantity = cart_item.quantity
                    break
        return render(request,'index.html',{'items':items})

'''view for login user
    if user is super_user, it will redirect to inventory page
    if other user try to login, redirect to index page with cart adding options'''
def loginView(request):
    if request.method=='GET':
        return render(request,'login.html',{'form':AuthenticationForm})
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            super_user=user.super_user
            if super_user==1:
                login(request,user)
                return redirect('inventory')
            else:
                login(request,user)
                return redirect('index')
        else:
            return HttpResponse('not valid')  

'''Create user view
    both super_user and others can be created'''
def SignUpView(request):
    if request.method=='GET':
        return render(request,'user_register.html',{'form':RegistrationForm})
    elif request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse('not valid')

#logout user
def logoutView(request):
    logout(request)
    return redirect('index')