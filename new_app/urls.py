from django.urls import path
from new_app import views, seller_views, buyer_views, admin_views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login_view/', views.Login, name='login_view'),

    # ADMIN
    path('admin_view/', admin_views.admin_viewbase, name='admin_view'),
    path('view_seller/', admin_views.view_seller, name='view_seller'),
    path('view_buyer/', admin_views.view_buyer, name='view_buyer'),
    path('delete_seller/<int:id>', admin_views.delete_seller, name='delete_seller'),
    path('delete_buyer/<int:id>', admin_views.delete_buyer, name='delete_buyer'),
    path('admin_view_productdetails', admin_views.admin_view_productdetails, name='admin_view_productdetails'),




    # Seller
    path('Seller_add/', seller_views.Seller_add, name='Seller_add'),
    path('seller_view/', seller_views.seller_viewbase, name='seller_view'),
    path('seller_profile_view/', seller_views.seller_profile_view, name='seller_profile_view'),
    path('edit_seller_profile/', seller_views.edit_seller_profile, name='edit_seller_profile'),
    path('add_product', seller_views.add_product, name='add_product'),
    path('view_product', seller_views.view_product, name='view_product'),
    path('delete_product/<int:id>', seller_views.delete_product, name='delete_product'),
    path('edit_product/<int:id>', seller_views.edit_product, name='edit_product'),


    # Buyer
    path('Buyer_add/', buyer_views.Buyer_add, name='Buyer_add'),
    path('buyer_view/', buyer_views.buyer_viewbase, name='buyer_view'),
    path('buyer_profile_view/', buyer_views.buyer_profile_view, name='buyer_profile_view'),
    path('edit_buyer_profile/', buyer_views.edit_buyer_profile, name='edit_buyer_profile'),
    path('buyer_view_productdetails/', buyer_views.buyer_view_productdetails, name='buyer_view_productdetails'),
    path('addtocart/<int:id>', buyer_views.addtocart, name='addtocart'),
    path('cart_view', buyer_views.cart_view, name='cart_view'),
    path('delete_cart/<int:id>', buyer_views.delete_cart, name='delete_cart'),
    path('BuyNowCart/<int:id>', buyer_views.BuyNowCart, name='BuyNowCart'),
    path('BuyNowHome/<int:id>', buyer_views.BuyNowHome, name='BuyNowHome'),
    path('Orders', buyer_views.Orders, name='Orders'),
    path('delete_order/<int:id>', buyer_views.delete_order, name='delete_order'),

]
