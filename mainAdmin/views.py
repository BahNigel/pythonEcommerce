import json
import os
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import productItems
from .models import cart, orderItem,CheckOut
from django.db.models import Sum



def shoe(request):
    items = productItems.objects.all()
    context = {'items': items}
    return render(request, 'shoe.html',context)


def index1(request):
    items = productItems.objects.all()
    context = {'items': items}
    return render(request, 'index1.html', context)


def index(request):
    return render(request, 'index.html')


def orders(request):
    return render(request, 'orders.html')


def products(request):
    items = productItems.objects.all()
    context = {'items': items}
    return render(request, 'products.html', context)


def brands(request):
    return render(request, 'brands.html')


def category(request):
    return render(request, 'category.html')


def customers(request):
    return render(request, 'customers.html')


def create(request):
    if request.method == "POST":
        items = productItems()
        items.name = request.POST.get('name')
        items.description = request.POST.get('description')
        items.price = request.POST.get('price')
        items.quantity = request.POST.get('qty')

        if len(request.FILES) != 0:
            items.image = request.FILES['image']

        items.save()
        messages.success(request, 'product inserted successfully')
        return redirect('/')
    return render(request, 'create.html')


def edit(request, pk):
    items = productItems.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(items.image) > 0:
                os.remove(items.image.path)
            items.image = request.FILES['image']
        items.name = request.POST.get('name')
        items.description = request.POST.get('description')
        items.price = request.POST.get('price')
        items.quantity = request.POST.get('qty')
        items.save()
        messages.success(request, "Product updated successfully")
        return redirect('/')
    context = {'items': items}
    return render(request, 'edit.html', context)


def singleProduct(request, pk):
    items = productItems.objects.get(id=pk)
    context = {'items': items}
    if request.method == "POST":
        if request.user.is_authenticated:
            if int(request.POST.get('qty')) > int(items.quantity):
                ids = str(items.id)
                return redirect('errorQuantity/' + ids)
            prod = cart()
            prod.name = items.name
            prod.description = items.description
            prod.price = items.price
            prod.qtyInSt = items.quantity
            prod.user = request.user
            qt = int(request.POST.get('qty'))
            pc = int(items.price)
            prod.total = (qt * pc)
            prod.quantity = request.POST.get('qty')
            prod.image = items.image
            prod.save()

            messages.success(request, "Item is added to cart")
            return redirect('/')
        else:
            return redirect('/login')

    return render(request, 'item.html', context)


def errorQuantity(request, pk):
    items = productItems.objects.get(id=pk)
    context = {'items': items}
    if request.method == "POST":
        prod = cart()
        prod.name = items.name
        prod.description = items.description
        prod.price = items.price
        prod.quantity = request.POST.get('qty')
        prod.save()
        messages.success(request, "Item is added to cart")
        return redirect('/')

    return render(request, 'errorQuantity.html', context)


def cartItems(request):
    prod = cart.objects.filter(user=request.user)
    context = {'prod': prod}
    return render(request, 'cart.html', context)


def deleteFromCart(request, pk):
    items = cart.objects.get(id=pk)
    items.delete()
    return redirect('cart')


def deleteFromOrder(request, pk):
    order = orderItem.objects.get(id=pk)
    order.delete()
    return redirect('placeOrderPage')


def updateCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    value = data['value']
    items = cart.objects.get(id=productId)
    items.quantity = value
    price = int(items.price)
    items.total = int(value) * price
    items.save()
    return JsonResponse('item was added', safe=False)


def placeOrder(request):
    data = json.loads(request.body)
    cartItem = cart.objects.filter(user=request.user)
    productId = data['productId']
    value = data['value']
    if request.method == "POST":
        for row in cartItem:
            items = orderItem()
            items.order_id = productId
            items.price = value
            items.name = row.name
            items.user = row.user
            items.image = row.image
            items.quantity = row.quantity
            items.total = row.total
            items.save()
            deleteItemFromCart = cart.objects.get(id=row.id)
            deleteItemFromCart.delete()

    return JsonResponse('item was added', safe=False)


def placeOrderPage(request):
    prod = orderItem.objects.filter(user=request.user)
    context = {'prod': prod}
    if request.method == 'POST':
        check = CheckOut()
        items = orderItem.objects.filter(user=request.user).first()
        check.checkoutId = items.order_id
        check.totalCheck = items.price
        check.firstName = request.POST.get('firstName')
        check.lastName = request.POST.get('lastName')
        check.userName = request.POST.get('userName')
        check.city = request.POST.get('city')
        check.state = request.POST.get('state')
        check.zip = request.POST.get('zip')
        check.paymentMethod = request.POST.get('paymentMethod')
        check.save()
        for row in prod:
            deleteItemFromCart = orderItem.objects.get(id=row.id)
            deleteItemFromCart.delete()
        return redirect('end')

    return render(request, 'placeOrder.html', context)


def end(request):
    return render(request, 'end.html')
