from django.shortcuts import render, redirect
from passlib.hash import sha512_crypt as sha512
from .models import User, Admin, Category, Product, Buy
import random
import string
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
import os





otp:str
username:str
email:str 
pwd :str 
country :str 
city :str 
dob :str 
state :str 
zipcode :str 
gender :str 
mobile :str 
address:str 

# Create your views here.

def index(request):
    laptop=Product.objects.filter(category='laptop')
    keyboard=Product.objects.filter(category='cables')
    ram=Product.objects.filter(category='memory')
    printer=Product.objects.filter(category='printer')
    graphic_card=Product.objects.filter(category='graphic Card')
    ssd=Product.objects.filter(category='ssd')
    hard_disk=Product.objects.filter(category='hard disk')
    monitor=Product.objects.filter(category='monitor')
    cpu=Product.objects.filter(category='cpu')
    power_supplies=Product.objects.filter(category='power supplies')
    motherboard=Product.objects.filter(category='motherboard')
    cabinet=Product.objects.filter(category='cabinet')
    cartridges=Product.objects.filter(category='cartridges')
    inks=Product.objects.filter(category='inks')
    note_machines=Product.objects.filter(category='note counting machines')
    mini_comp=Product.objects.filter(category='mini computers')
    hot= Product.objects.all().order_by('id')[:15][::-1]
    return render(request, 'index.html',{'category':Category.objects.all(),'laptop':laptop,'keyboard':keyboard,'ram':ram,'printer':printer,'graphic_card':graphic_card,'ssd':ssd,'hot':hot,'hard_disk':hard_disk,'monitor':monitor,'cpu':cpu,'power_supplies':power_supplies,'motherboard':motherboard,'cabinet':cabinet,'cartridges':cartridges,'inks':inks,'note_machines':note_machines,'mini_comp':mini_comp})

def redirectindex(request):
    return HttpResponseRedirect('/')

# User Login functions
def login(request):
    return render(request,'login.html')

def login_check(request):
    user=request.POST['user']
    pwd=request.POST['pwd']
    user=user.lower()
    print(user)
    pwd=sha512.hash(pwd, rounds=5000,salt="latticeapp")
    if User.objects.filter(name=user,password=pwd).exists():
        member=User.objects.get(name=user,password=pwd)
        key=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(30))
        request.session['private_lattice_key']=key
        member.private_key=key
        member.save()
        return redirect('index/'+key+'/')
    elif User.objects.filter(email=user,password=pwd).exists():
        member=User.objects.get(email=user,password=pwd)
        key=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(30))
        request.session['private_lattice_key']=key
        member.private_key=key
        member.save()
        return redirect('index/'+key+'/')
    else:
        messages.info(request,"Wrong username or password")
        return redirect('login')

def login_verified(request,member):
    member=User.objects.get(private_key=member)
    if member.private_key==request.session['private_lattice_key']:
        return render(request,'index.html',{'member':member})


# User signup functions
def signup(request):
    return render(request,'signup.html')

def checkmail(request):
    username=request.POST['username']
    email=request.POST['email']
    pwd=request.POST['pwd']
    country=request.POST['country']
    city=request.POST['city']
    dob=request.POST['dob']
    state=request.POST['state']
    zipcode=request.POST['zipcode']
    mobile=request.POST['mobile']
    address=request.POST['address']
    state=request.POST['state']
    global otp
    otp=''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
    return render(request,'otp.html')

def checkotp(request):
    otp1=request.POST['otp']
    global otp, username, email, pwd, country, city, dob, state, zipcode, gender, mobile, address
    if str(otp)==str(otp1):
        pwd=sha512.hash(pwd, rounds=5000,salt="latticeapp")
        User.objects.create(name=username,email=email,password=pwd,address='',mobile='',city='',state='',zipcode='',country='',gender='',dob='')
        return redirect('login')
#Admin login functions
def admin_login(request):
    return render(request,'admin_login.html')

def admin_check(request):
    user=request.POST['input_usernamebox']
    pwd=request.POST['input_passwordbox']
    user=user.lower()
    pwd=sha512.hash(pwd, rounds=5000,salt="latticeadmin")
    if Admin.objects.filter(name=user,password=pwd).exists():
        member=Admin.objects.get(name=user,password=pwd)
        key=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(30))
        request.session['private_lattice_key']=key
        member.private_key=key
        member.save()
        return redirect('admin_user_verified/'+key+'/')
    elif Admin.objects.filter(email=user,password=pwd).exists():
        member=Admin.objects.get(email=user,password=pwd)
        key=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(30))
        request.session['private_lattice_key']=key
        member.private_key=key
        member.save()
        return redirect('admin_user_verified/'+key+'/')
    else:
        messages.info(request,"Wrong username or password")
        return redirect('admin_login')

def admin_user_verified(request,member):
    member=Admin.objects.get(private_key=member)
    if member.private_key==request.session['private_lattice_key']:
        product=Product.objects.all()
        return render(request,'admin.html',{'member':member,'products':product})


# Contact page 
def contact(request):
    return render(request,'contact.html')
 
def contact_sendmail(request):
    messages.info(request,"Mail Sent")
    return redirect('contact')

# Product page
def viewproduct(request):
    product=Product.objects.get(id=request.GET['productid'])
    name=product.name
    tags=product.tags.split(',')
    imgpath=product.img
    price=product.price
    features=product.features.split('||')
    desc=product.desc
    id=product.id
    return render(request,'product.html',{'product':product,'name':name,'tags':tags,'imgpath':imgpath,'price':price,'features':features,'desc':desc,'id':id})

#Add product page
def addproductpage(request,member):
    return render(request,'addproductpage.html',{'category':Category.objects.all(),'member':Admin.objects.get(private_key=member)})

def add_product_to_database(request, member):
    name=request.POST['name']
    price=request.POST['price']
    description=request.POST['description']
    quantity=request.POST['quantity']
    category=request.POST['category']
    other_category=request.POST['other_category']
    other_category=other_category.lower().strip()
    discount=request.POST['discount']
    tags=request.POST['tags']
    feature=request.POST['features']
    feature=feature.replace(';','||')
    img=request.FILES['image']
    newimgname="static/images_for_staticpurpose/"+img.name
    if not os.path.exists(newimgname):
        print(os.path.exists(newimgname))
        print(newimgname)
        file_name = FileSystemStorage().save("lattice_app/static/images_for_staticpurpose/"+img.name, img)
    if not Category.objects.filter(name=other_category).exists():
        category2=Category(name=other_category)
        category2.save()
        category=other_category

    member=Admin.objects.get(private_key=member)
    if member.private_key==request.session['private_lattice_key']:
         product=Product(name=name,price=price,desc=description,img=newimgname,quantity=quantity,category=category.lower(),discount=discount,tags=tags.lower(),features=feature)
         product.save()
         return HttpResponseRedirect('addproductpage')
    return HttpResponseRedirect('admin_user_verified/<str:member>')

def addimagebystatic(request,member):
    return render(request,'addimagebystatic.html')

def addstaticimage_file(request,member):
    img=request.FILES.getlist('file')
    for x in img:
        file_name = FileSystemStorage().save("lattice_app/static/images_for_staticpurpose/"+x.name, x)
    return render (request,'addimagebystatic.html')

def deleteproductfromdatabase(request,member):
    idd=request.POST['id']
    Product.objects.filter(id=idd).delete()
    return redirect('admin_user_verified/<str:member>')

def searchproduct(request):
    search=request.GET['search']
    category=request.GET['category']
    search=search.lower()
    category=category.lower()
    if search!="" and category!="":
        products=Product.objects.all()
        if category!="all":
            products=products.filter(category=category)
        else:
            for x in products:
                tags=x.tags.split(',')
                for y in tags:
                    z=y.lower()
                    if z.strip()==search:
                        products=products.filter(category=x.category)
        return render(request,'product_page.html',{'products':products,'search':search,'category':category})
    return render(request,'product_page.html')

if_for_checkout="nill"  
def checkout(request):
    idd=request.POST['id']
    global id_for_checkout
    id_for_checkout=str(idd)
    pathtogoto='checkoutpage'
    return JsonResponse(pathtogoto,safe=False)
    #return render(request,'checkout.html',{'product':product,'name':name,'tags':tags,'imgpath':imgpath,'price':price,'features':features,'desc':desc,'id':id})

def checkoutpage(request):
     global id_for_checkout
     print(id_for_checkout)
     product=Product.objects.get(id=id_for_checkout)
     name=product.name
     tags=product.tags.split(',')
     imgpath=product.img
     price=product.price
     features=product.features.split('||')
     desc=product.desc
     id=product.id
     return render(request,'checkout.html',{'product':product,'name':name,'tags':tags,'imgpath':imgpath,'price':price,'features':features,'desc':desc,'id':id})


def addtobuy(request):
    productid=request.POST['productid']
    product=Product.objects.get(id=productid)
    username=request.POST['username']
    phone=request.POST['phone']
    email=request.POST['email']
    address= request.POST['address']
    city=request.POST['city']
    state=request.POST['state']
    postal=request.POST['postal']
    if User.objects.filter(email=email).exists():
        user=User.objects.get(email=email)
        Buy.objects.create(product_name=product.name,product_id=productid, price=product.price,discount=product.discount,username=user.name,user_id=user.id,quantity=1)
    
    else:
        User.objects.create(name=username,mobile=phone,country="india",password="NonGuessablePaswordForEarlyDeployment",dob="mock",gender="mock",private_key="null",email=email,address=address,city=city,state=state,zipcode=postal)
        user=User.objects.get(email=email)
        Buy.objects.create(product_name=product.name,product_id=productid, price=product.price,discount=product.discount,username=user.name,user_id=user.id,quantity=1)
    
    # get user data save to user database then get product id user id etc save to bought database
    return JsonResponse('index',safe=False)

def adminseeorders(request,member):
    buy=Buy.objects.all()
    return render(request,'admin_buy.html',{'member':member,'buy':buy})

def seesinglebuy(request,member,buyid):
    buy=Buy.objects.get(id=buyid)
    product=Product.objects.get(id=buy.product_id)
    user=User.objects.get(id=buy.user_id)
    return render(request,'admin_buy_single.html',{'member':member,'buy':buy,'user':user,'product':product})


def deleteproductbuy(request,member,buyid):
    Buy.objects.filter(id=buyid).delete()
    return redirect('admin_user_verified/<str:member>')