from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Order, Customer


def loginpage(request):
    if request.user.is_authenticated:
        cust = get_object_or_404(Customer, Firstname=request.user.username)
        cid = cust.id
        return redirect('/wholesale/customer/' + str(cid) + '/')
    else:
        return render(request, 'wholesale/loginpage.html')


def loginauth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        cust = get_object_or_404(Customer, Firstname=username)
        cid = cust.id
        return redirect('/wholesale/customer/' + str(cid) + '/')

    else:
        return redirect('/wholesale/invalidlogin/')


def invalidlogin(request):
    if request.user.is_authenticated:
        cust = get_object_or_404(Customer, Firstname=request.user.username)
        cid = cust.id
        return redirect('/wholesale/customer/' + str(cid) + '/')
    else:
        return render(request, 'wholesale/invalidlogin.html')


def logoutauth(request):
    logout(request)
    return render(request, 'wholesale/logout.html')


def customerpage(request, cid):
    if request.user.is_authenticated:
        cust = get_object_or_404(Customer, id=cid)
        corders = Order.objects.filter(Cid=cust)
        products = Product.objects.all()
        context = {'cust': cust, 'corders': corders, 'products': products}
        return render(request, 'wholesale/customerpage.html', context)
    else:
        return redirect('/wholesale/invalidlogin/')


def customerorder(request, cid):
    if request.user.is_authenticated:
        cust = get_object_or_404(Customer, id=cid)
        products = Product.objects.all()
        context = {'cust': cust, 'products': products}
        return render(request, 'wholesale/customerorder.html', context)
    else:
        return redirect('/wholesale/invalidlogin/')


def placeorder(request, cid):
    if request.user.is_authenticated:
        cust = get_object_or_404(Customer, id=cid)
        ans = request.POST['product']
        prod = get_object_or_404(Product, id=ans)
        qty = request.POST['quantity']
        o = Order(Pid=prod, Cid=cust, Qty=qty)
        o.save()
        return redirect('/wholesale/customer/' + str(cid) + '/')
    else:
        return redirect('/wholesale/invalidlogin/')
