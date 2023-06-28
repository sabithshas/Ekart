from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import userregister,Products,Cart
from django.contrib.auth import authenticate, login as auth_login
# Create your views here.
def home(request):
    return render(request,'Home.html')
def Register(request):
    return render(request,'Register.html')
def login(request):
    return render(request,'login.html')
def shopping(request):
    productdata = Products.objects.all()
    return render(request, 'shopping.html', {'data': productdata})
   

def bregister(request):
    if request.method =="POST":
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        username=request.POST["username"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        role='customer'
        password=request.POST["password"]
        confirmpassword=request.POST["Confirmpassword"]
        print(firstname)
        if password==confirmpassword:
            if User.objects. filter (username=username) .exists() :
                messages. info(request, "Username taken")
                return redirect('register')

            else:   
                user=User.objects.create(username=username, password=password)
                user. save()
                data=userregister.objects.create(user=user,firstname=firstname,lastname=lastname,username=username,email=email,phone=phone,role=role,password=password,confirmpassword=confirmpassword)
                data.save()
                print(data,'hii')
        else: 
            return render(request,'Register.html')

        return redirect('login')
    else:
        return render(request,'Register.html')
        
# 

def loginuser(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        print("hi",user)
        data=User.objects.filter(username=username).values()
        role=''
        for i in data:
            u_name=i["username"]
            print(u_name)
            userdata=userregister.objects.filter(username=username).values()
            for i in userdata:
                role=i['role']
            if user is not None and username==u_name and role=='customer':
                auth_login(request,user)
            return redirect('shopping')   
        else:
            return render(request,'login.html') 
    else:
            return render(request,'login.html')
    

def product(request):
    return render(request,'addproduct.html')

def addproduct(request):

    if request.method == 'POST':
        productname = request.POST['productname']
        category = request.POST['category']
        price = request.POST['price']
        description = request.POST['description']
        productimage = request.FILES['productimage']

        data = Products(productname=productname, category=category,
                        price=price, description=description, productimage=productimage)
        data.save()

        return redirect('viewproductpage')
    else:
        return render(request,'addproduct.html')

def viewproductpage(request):
    productdata = Products.objects.all()
    return render(request, 'viewproducts.html', {'data': productdata})

def productedit(request,product_id):
    data=Products.objects.get(id=product_id)
    return render(request,'editproducts.html',{"data":data})

def productupdate(request, product_id):
    data = Products.objects.get(id=product_id)
    data.productname = request.POST['productname']
    data.category = request.POST['category']
    data.price = request.POST['price']
    data.description = request.POST['description']
    data.productimage = request.FILES['productimage']
    data.save()
    return redirect('viewproductpage')

def deleteproduct(request, product_id):
    data = Products.objects.get(id=product_id)
    data.delete()
    return redirect('viewproductpage')



def mycart(request):
    cart_data = Cart.objects.filter(user=request.user)
    total=0
    for i in cart_data:
        total+=i.quantity*i.product.price

    all_data={'data':cart_data,'total':total}

    print('total',total)

    return render(request, 'mycart.html', all_data)

def addtocart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(
        product=product, user=request.user, quantity=0)
    cart.quantity += 1
    cart.save()
    return redirect('shopping')

def removefromcart(request, product_id):
    product =Cart.objects.get(id=product_id)
    product.delete()
    return redirect('mycart')