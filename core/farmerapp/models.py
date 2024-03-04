from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse

def profile_image_upload_path(instance, filename):
    # ফাইলটি ব্যবহারকারীর নাম ভিত্তিক একটি ফোল্ডারে আপলোড করো
    return f"media/profileimage/{instance.username}/{timezone.now().strftime('%Y%m%d%H%M%S')}-{filename}"


class Custom_User(AbstractUser):
    USER=[
        ('farmer','Farmer'),
        ('user','User'),
        ('agent','Agent'),
        ('admin','Admin'),
        ('seller','Seller'),
        
    ]
    
    display_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number = models.CharField(max_length=11,blank=True, null=True)
    password=models.CharField(max_length=100)
    user_type=models.CharField(choices=USER, max_length=120)
    profile_image = models.ImageField(upload_to=profile_image_upload_path, null=True)
    present_address = models.CharField(max_length=255, blank=True, null=True)
    Shop_name=models.CharField(max_length=100, blank=True, null= True)
    permanent_address = models.CharField(max_length=255, blank=True, null=True)
    farm_area_adress = models.CharField(max_length=255, blank=True, null=True)  
    nid_photo = models.ImageField(upload_to='media/nid_photos', null=True, blank=True)
    details = models.TextField(blank=True, null=True)
    otp_token = models.CharField(max_length = 6, blank = True, null = True)
    
    
    
class post_product(models.Model):
    Created_By=models.ForeignKey(Custom_User, on_delete=models.CASCADE, null=True)
    Create_at=models.DateTimeField(auto_now_add=True, null=True)
    Product_Image=models.ImageField(upload_to="media/postimages", null=True)
    Product_Title=models.CharField(max_length=100)
    Product_Description=models.TextField(max_length=5000) 
    Product_price=models.CharField(max_length=5000, null=True) 
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    CATEGORY_CHOICES = [
        ('vegetables', 'Vegetables'),
        ('fishes', 'Fishes'),
        ('meats', 'Meat'),
        ('fruits', 'Fruits'),
    ]

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20, default='none')
    Permission=models.BooleanField(default=False)
    
    def __str__(self):
        return self.Product_Title
    
    


class CartItem(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(post_product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * float(self.product.Product_price)
    
class Add_CartItem(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(post_product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__ (self):
        return self.user.display_name
    
class WishlistItem(models.Model):
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    product = models.ForeignKey(post_product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.display_name}'s Wishlist - {self.product.Product_Title}"
