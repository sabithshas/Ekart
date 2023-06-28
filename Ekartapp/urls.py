from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home,name='home'),
    path("home/",views.home,name='home'),
    path("register/",views.Register,name='register'),
    path("login/",views.login,name='login'),
    path("userregister/",views.bregister,name='userregister'),
    path("shopping/",views.shopping,name='shopping'),
    path('loginuser/',views.loginuser,name="loginuser"),
    path('product',views.product,name="product"),
    path('addproduct',views.addproduct,name="addproduct"),
    path('viewproductpage',views.viewproductpage,name="viewproductpage"),
    path('<int:product_id>/productedit',views.productedit,name='productedit'),
    path('<int:product_id>/productupdate',views.productupdate,name='productupdate'),
    path('deleteproduct/<int:product_id>',views.deleteproduct,name='deleteproduct'),
    path("mycart",views.mycart,name='mycart'),
    path('addtocart/<int:product_id>',views.addtocart,name='addtocart'),
     path('removefromcart/<int:product_id>',views.removefromcart,name='removefromcart'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)