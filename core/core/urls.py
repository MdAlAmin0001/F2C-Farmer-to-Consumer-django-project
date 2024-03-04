"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from farmerapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signuppage, name="signuppage"),
    path('loginpage/', loginpage, name="loginpage"),
    path('homepage/', homepage, name="homepage"),
    path('shoppage/', shoppage, name="shoppage"),
    path('logoutpage/', logoutpage, name="logoutpage"),
    path('profile/', profile, name="profile"),
    path('addproduct/', addproduct, name="addproduct"),
    path('updateproduct/', updateproduct, name="updateproduct"),
    path('delete_product/<str:id>', delete_product, name="delete_product"),
    path('editproduct/<str:id>', editproduct, name="editproduct"),
    path('Product_details/<str:id>', Product_details, name="Product_details"),
    path('permission_product/', permission_product, name="permission_product"),
    path('permissioned/<str:id>', permissioned, name="permissioned"),
    path('permissioned_denied/<str:id>', permissioned_denied, name="permissioned_denied"),

    path('search_query/', search_query, name="search_query"),
    path('forgetpassword/', forgetpassword, name="forgetpassword"),
    path('changepassword/', changepassword, name="changepassword"),
    
    # path('cart/', cart, name='cart'),
    path('vegetables/', vegetables, name='vegetables'),
    path('fishes/', fishes, name='fishes'),
    path('meats/', meats, name='meats'),
    path('fruits/', fruits, name='fruits'),
    path('profile_update/', profile_update, name='profile_update'),
    
    path('add_to_cart/<str:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<str:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', view_cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    
    path('wishlist/', wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:item_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
