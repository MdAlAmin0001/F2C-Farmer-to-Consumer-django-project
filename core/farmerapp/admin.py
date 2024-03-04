from django.contrib import admin

from .models import *

class Custom_User_Display(admin.ModelAdmin):
    list_display=['display_name','email','user_type']
    
class post_product_Display(admin.ModelAdmin):
    list_display=['Created_By','Product_Title','Create_at']
    
admin.site.register(Custom_User,Custom_User_Display)
admin.site.register(post_product,post_product_Display)
admin.site.register(Add_CartItem)
