from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .froms import ItemForm
from .models import Cart, Item
from django.contrib.auth.decorators import login_required

#create item 
def createItemView(request):
    if request.method == 'GET':
        return render(request, 'add_item.html', {'form': ItemForm})
    elif request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('inventory')
        else:
            print(form.errors)
            return HttpResponse('not valid')

'''add item to user cart
    check whether the item already in cart and 
    user is logged in or not'''
def add_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            qty = 1
            pid = request.POST.get('pid')
            item_obj = Item.objects.get(id=pid)
            carts = Cart.objects.filter(user=request.user, item=item_obj).values('quantity')
            for item in carts:
                qty = item['quantity']
            if (Cart.objects.filter(user=request.user.id, item=pid)):
                return JsonResponse({'status': "item already in cart", 'quantity': qty})
            else:
                Cart.objects.create(user=request.user,
                                    item=item_obj, quantity=1)
                return JsonResponse({'status': "item added to cart", 'quantity': qty})
        else:
            return JsonResponse({'status': "please login"})

#view items that added to cart
def showCart(request):
    carts = Cart.objects.all()
    return render(request, 'cart.html', {'carts': carts})

#remove item from user cart
def remove_cart(request, id):
    if request.method == 'GET':
        cart = Cart.objects.get(pk=id)
        cart.delete()
        return redirect('cartdata')

'''increase item quantity in cart
    check the quantity of item and add 1 to it while clicking '+' button
    and return updated quantity to template
    by using jquery and ajax'''
def cart_plus(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        item_obj = Item.objects.get(id=pid)
        carts = Cart.objects.filter(
            user=request.user,
            item=item_obj).values('quantity')

        for item in carts:
            qty = item['quantity']

        if carts:
            Cart.objects.filter(
                user=request.user,
                item=item_obj).update(quantity=qty+1)

        carts = Cart.objects.filter(
            user=request.user,
            item=item_obj).values('quantity')

        qty = carts[0]
        return JsonResponse({'quantity': qty})

'''decrease item quantity in cart
    check the quantity of item and substitute 1 from it while clicking '-' button
    and return updated quantity to template
    by using jquery and ajax'''
def cart_minus(request):
    if request.method == 'POST':
        pid = request.POST.get('pid')
        item_obj = Item.objects.get(id=pid)
        carts = Cart.objects.filter(
            user=request.user,
            item=item_obj).values('quantity')
        for item in carts:
            qty = item['quantity']

        if carts:
            if qty==0:
                Cart.objects.filter(user=request.user.id,item=item_obj.id).delete()
            else:
                Cart.objects.filter(user=request.user,item=item_obj.id).update(quantity=qty-1)

        carts = Cart.objects.filter(
                user=request.user, 
                item=item_obj).values('quantity')

        qty = carts[0]
        data=qty['quantity']
        return JsonResponse({'quantity': data})

#inventory home page 
@login_required
def inventoryHome(request):
    if request.method=='GET':
        items=Item.objects.all()
        return render(request,'inventory.html',{'items':items})

#update item in inventory list view
def inventoryUpdate(request,id):
    if request.method=='POST':
        form=ItemForm(request.POST,request.FILES,instance=Item.objects.get(pk=id))
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form=ItemForm(instance=Item.objects.get(pk=id))
        return render(request,'inventoryUpdate.html',{'form':form})

#delete item from inventory
def inventoryDelete(request,id):
    obj=Item.objects.get(pk=id)
    obj.delete()
    return redirect('inventory')
