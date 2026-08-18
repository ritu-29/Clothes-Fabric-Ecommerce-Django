"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp import views

if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.index, name='index'),
        path('about', views.about, name='about'),
        path('contact', views.contact, name='contact'),
        path('login', views.login, name='login'),
        path('signup', views.signup, name='signup'),
        path('logout', views.logout, name='logout'),
        path('forgotpassword', views.forgotpassword, name='forgotpassword'),
        path('adduserdetail', views.adduserdetail, name='adduserdetail'),
        path('showuser', views.showuser, name='showuser'),
        path('editprofile', views.editprofile, name='editprofile'),
        path('update', views.update, name='update'),
        path('addseller', views.addseller, name='addseller'),
        path('showseller', views.showseller, name='showseller'),
        path('editsellerdetail', views.editsellerdetail, name='editsellerdetail'),
        path('updateseller', views.updateseller, name='updateseller'),
        path('product_form', views.product_form, name='product_form'),
        path('edit_product/<int:ep>', views.edit_product, name='edit_product'),
        path('update_product', views.update_product, name='update_product'),
        path('products', views.products, name='products'),
        path('shopdetail/<int:product_id>', views.shopdetail, name='shopdetail'),
        path('add_to_cart', views.add_to_cart, name='add_to_cart'),
        path('ecommerce-cart', views.ecommerce_cart, name='ecommerce-cart'),
        path('increaseitem/<int:id>', views.increaseitem, name="increseitem"),
        path('decreaseitem/<int:id>', views.decreaseitem, name="decreseitem"),
        path('update_product_quantity/', views.update_product_quantity, name='update_product_quantity'),
        path('removefromcart/<int:id>', views.removefromcart, name='removefromcart'),
        path('payment-status/', views.success, name='payment_status'),
        path('complaint_submit', views.complaint_submit, name='complaint_submit'),
        path('storefeedback', views.storefeedback, name='storefeedback'),
        path('payment', views.payment, name='payment'),
        path('vieworder/<int:id>', views.vieworder, name='vieworder'),
        path('sellerproduct', views.sellerproduct, name='sellerproduct'),
        path('deleteProduct/<int:eid>', views.deleteProduct, name='deleteProduct'),
        path('showorder', views.showorder, name='showorder'),
        path('find_products', views.find_products, name='find_products'),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
