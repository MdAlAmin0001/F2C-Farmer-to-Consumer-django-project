import random
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,login,logout
from farmerapp.models import *
from django.contrib.auth.decorators import login_required
from core.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.


def signuppage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        display_name=request.POST.get('displayName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        User_type=request.POST.get('userType')
        Profile_Image=request.FILES.get('profilePhoto')
        
        user=Custom_User.objects.create_user(username=username,password=password)
        user.display_name=display_name
        user.email=email
        user.user_type=User_type
        user.profile_image=Profile_Image
        user.save()
        return redirect('loginpage')
    return render(request,"signuppage.html")


def loginpage(request):
    if request.method == 'POST':
        myusername=request.POST.get('username')
        mypassword=request.POST.get('password')
        
        user = authenticate(request, username=myusername, password=mypassword)
        
        if user:
            login(request, user)
            return redirect("shoppage")
    return render(request, "loginpage.html")



def logoutpage(request):
    logout(request)
    return redirect("loginpage")

@login_required
def homepage(request):
    featured_products = post_product.objects.filter(category='vegetables', Permission=True).order_by('-Create_at')[:3]
    featured_products2 = post_product.objects.filter(category='fishes', Permission=True).order_by('-Create_at')[:3]
    featured_products3 = post_product.objects.filter(category='meats', Permission=True).order_by('-Create_at')[:3]
    featured_products4 = post_product.objects.filter(category='fruits', Permission=True).order_by('-Create_at')[:3]
    context = {
        'featured_products': featured_products,
        'featured_products2':featured_products2,
        'featured_products3':featured_products3,
        'featured_products4':featured_products4,
    }
    return render(request, "Home.html", context)


@login_required
def shoppage(request):
    product=post_product.objects.filter(Permission=True).order_by('-Create_at')
    context={
        'pkey':product
    }
    return render(request, "Shop.html", context)

@login_required
def profile(request):
    return render(request, "Profile.html")

@login_required
def profile_update(request):
    user = request.user

    if request.method == 'POST':
     
        display_name = request.POST.get('name')
        email = request.POST.get('email')
        present_address = request.POST.get('p_address')
        phone_number = request.POST.get('phone')
        profile_image = request.FILES.get('image')
        permanent_address = request.POST.get('per_address')
        farm_area_address = request.POST.get('farm_area')
        nid_image = request.FILES.get('nid')  
        details = request.POST.get('details')

        
        user.display_name = display_name
        user.email = email
        user.present_address = present_address
        user.phone_number = phone_number
        user.permanent_address = permanent_address
        user.farm_area_adress = farm_area_address
        user.details = details
        
        if profile_image:
            user.profile_image = profile_image

       
        if nid_image:
            user.nid_photo = nid_image

        user.save()
        return redirect('profile')
    
@login_required
def addproduct(request):
    if request.method == "POST":
        product_image=request.FILES.get('productPhoto')
        product_title=request.POST.get('productName')
        product_description=request.POST.get('productDescription')
        product_price=request.POST.get('productPrice')
        product_quantity=request.POST.get('quantity')
        category=request.POST.get('category')
        Create_by=request.user
        
        product=post_product(
            Product_Image=product_image,
            Product_Title=product_title,
            Product_Description=product_description,
            Product_price=product_price,
            quantity=product_quantity,
            category=category,
            Created_By=Create_by
        )
        
        product.save()
        return redirect('shoppage')    
    return render(request, "addproduct.html")
@login_required
def editproduct(request, id):
    prod=post_product.objects.filter(id=id)
    context={
        'prod':prod
    }
    return render(request,'updateproduct.html', context)

@login_required
def updateproduct(request):
    if request.method == "POST":
        product_id = request.POST.get('productid')
        product_image = request.FILES.get('productPhoto')
        product_title = request.POST.get('productName')
        product_description = request.POST.get('productDescription')
        product_price = request.POST.get('productPrice')
        product_quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        created_by = request.user
        
      
        product = post_product.objects.get(id=product_id)

      
        product.Product_Title = product_title
        product.Product_Description = product_description
        product.Product_price = product_price
        product.quantity = product_quantity
        product.category = category
        product.Created_By = created_by

       
        if product_image:
            product.Product_Image = product_image
        product.save()

        return redirect('shoppage')
@login_required
def delete_product(request, id):
    prod = post_product.objects.filter(id=id)
    prod.delete()
    return redirect('shoppage')

@login_required
def Product_details(request,id):
    product = get_object_or_404(post_product, id=id)
    product.save()
    return render(request, 'Product_details.html', {'product': product})

#product permission approve or denied function start
@login_required
def permission_product(request):
    product=post_product.objects.filter(Permission=False)
    context={
        'pkey':product
    }
    return render(request,"approveproduct.html", context)

@login_required
def permissioned(request,id):
    product=post_product.objects.get(id=id)
    product.Permission=True
    product.save()
    
    return redirect('permission_product')
@login_required
def permissioned_denied(request,id):
    product=post_product.objects.get(id=id)
    
    product.delete()
    
    return redirect('permission_product')
#product permission approve or denied function end





@login_required
def search_query(request):
    if request.method == 'POST':
        query=request.POST.get('search')
        search_post=post_product.objects.filter(
            Q(Product_Title__icontains=query) | Q(Product_Description__icontains=query)
        )
    return render(request, 'Shop.html',{'sq':search_post})


def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Custom_User.objects.get(email=email)
            otp = random.randint(111111, 999999)
            user.otp_token = otp
            user.save()

            sub = f"Your Otp:{otp}"
            msg = f"""Dear User,
            Your OTP is:{otp}. Please keep it secret"""
            from_mail = EMAIL_HOST_USER
            recipient = [email]
            send_mail(
                subject=sub,
                recipient_list=recipient,
                from_email=from_mail,
                message=msg,
            )
            return render(request, 'changepassword.html', {'email': email})
        except Custom_User.DoesNotExist:
            # Email not found in the database
            message = "Email address not found. Please check and try again."
            return render(request, 'forgetpassword.html', {'error_message': message})
    else:
        return render(request, 'forgetpassword.html')


def changepassword(request):
    if request.method == "POST":
        mail = request.POST.get('email')
        otp = request.POST.get('otp')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        user = Custom_User.objects.get(email = mail)
        if user.otp_token != otp:
            return redirect('forgetpassword')
        if password != c_password:
            return redirect('forgetpassword')
        user.set_password(password)
        
        user.save()
        return redirect('loginpage')
    return render(request, 'changepassword.html')
@login_required
#show products as category
def vegetables(request):
    products = post_product.objects.filter(category='vegetables', Permission=True).order_by('-Create_at')
    context = {
        'products': products
    }
    return render(request, 'vegetables.html', context)
@login_required
def fishes(request):
    products = post_product.objects.filter(category='fishes', Permission=True).order_by('-Create_at')
    context = {
        'products': products
    }
    return render(request, 'fishes.html', context)
@login_required
def meats(request):
    products = post_product.objects.filter(category='meats', Permission=True).order_by('-Create_at')
    context = {
        'products': products
    }
    return render(request, 'meats.html', context)
@login_required
def fruits(request):
    products = post_product.objects.filter(category='fruits', Permission=True).order_by('-Create_at')
    context = {
        'products': products
    }
    return render(request, 'fruits.html', context)

# cart system start
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(post_product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"{product.Product_Title} added to your cart.")
    else:
        messages.success(request, f"{product.Product_Title} added to your cart.")

    return redirect('shoppage')

@login_required
def remove_from_cart(request, product_id):
   
    prod=CartItem.objects.filter(id = product_id)
    prod.delete()
    return redirect('cart')


@login_required
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'cart.html', context)

# You can create a separate view for the checkout process.
# This might involve creating an order and handling payment.
# For simplicity, I'll leave this as a placeholder.
@login_required
def checkout(request):
    # Your checkout logic goes here
    # This could involve creating an order, handling payment, etc.
    # For simplicity, I'm leaving this as a placeholder.
    messages.success(request, "Checkout is not implemented in this example.")
    return redirect('shoppage')

@login_required
def wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, product_id):
    product = post_product.objects.get(pk=product_id)
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        # Item already exists in the wishlist, you may want to handle this case differently
        pass

    return redirect('shoppage')

@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = WishlistItem.objects.get(pk=item_id)
    wishlist_item.delete()
    return redirect('wishlist')