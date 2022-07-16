
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
     # Index page paths
     path('', views.index,name='index'),
     path('index', views.index,name='index'),
     path('viewproduct/index', views.redirectindex,name='index'),

     # # viewproduct forwarding links
     path('checkout', views.checkout,name='checkout'),
     path("checkoutpage", views.checkoutpage, name="checkoutpage"),
     path("addtobuy", views.addtobuy, name="addtobuy"),
     # path("viewproduct/contact", views.contact, name="contact"),
     # path("viewproduct/contact_sendmail", views.contact_sendmail, name="contact_sendmail"),

     # Product page
     path('viewproduct', views.viewproduct,name='viewproduct'),
     path('searchproducts', views.searchproduct,name='searchproducts'),


     # User login paths
     path('login', views.login,name='login'),
     path('login_check', views.login_check,name='login_check'),
     #path('index/<str:member>/', views.login_verified,name='login_verified'),

     # User signup
     path('signup', views.signup,name='signup'),
     path('checkmail', views.checkmail,name='checkmail'),


     # Contact page paths
     path("contact", views.contact, name="contact"),
     path("contact_sendmail", views.contact_sendmail, name="contact_sendmail"),

     # Admin login
     path('admin_login', views.admin_login,name='admin_login'),
     path('admin_check', views.admin_check,name='admin_check'),
     path('admin_user_verified/<str:member>/', views.admin_user_verified,name='admin_user_verified'),
     path('admin_user_verified/<str:member>/a', views.admin_user_verified,name='admin_user_verified'),


     #Addproduct
     path('admin_user_verified/<str:member>/addproductpage', views.addproductpage,name='addproductpage'),
     path('admin_user_verified/<str:member>/add_product_to_database', views.add_product_to_database,name='add_product_to_database'),
     path('admin_user_verified/<str:member>/addimagebystatic', views.addimagebystatic,name='addimagebystatic'),
     path('admin_user_verified/<str:member>/addstaticimage_file', views.addstaticimage_file,name='addstaticimage_file'),
     path('admin_user_verified/<str:member>/deleteproductfromdatabase', views.deleteproductfromdatabase,name='deleteproductfromdatabase'),

     # Bought Items
     path('admin_user_verified/<str:member>/adminseeorders', views.adminseeorders,name='adminseeorders'),
     path('admin_user_verified/<str:member>/seesinglebuy/deleteproductbuy/<str:buyid>', views.deleteproductbuy,name='deleteproductbuy'),
     path('admin_user_verified/<str:member>/seesinglebuy/<str:buyid>', views.seesinglebuy,name='seesinglebuy'),
     

     


]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
"""access static files"""