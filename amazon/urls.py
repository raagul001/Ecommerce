from django.urls import path
from . import views

urlpatterns = [
    path('',views.Purchase,name='home'),
    path('register',views.Register,name='register'),
    path('login',views.Login_page,name='login'),
    path('logout',views.Logout_page,name='logout'),
    path('cart',views.cart_view,name='cart'),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('remove_cart/<str:cid>',views.Remove_cart,name='remove_cart'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:name>',views.details,name='collections'),
    path('collections/<str:cname>/<str:pname>',views.product_details,name='product_details'),
    path('addtocart',views.add_to_cart,name='addtocart'),

]
