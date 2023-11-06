from home.views import *
from product.views import *
from my_product.views import *
from users.views import *
from django.urls import path

urlpatterns = [
 
    path('category/add', create_category),
    path('categorys/', list_categories),
    path('category/<int:id>/', details_categories),
    path('category/update/<int:id>', update_category),
    path('category/<int:id>/delete',delete_items),
    
    path('sub-category/add', create_product),
    path('sub-category/', product_list),
    path('sub-category/<int:id>/', product_details),
    path('sub-category/update/<int:id>', update_product),
    path('sub-category/<int:id>/delete',delete_product),
    
    
     path('product/add', product_add),
     path('products', product_list),
     path('product/details/<int:id>', product_details),
     path('product/update/<int:id>', product_update),
     path('product/<int:id>/delete',delete_product),
     
     
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
   #path('user', UserView.as_view()),
    
     
     
     
     
     
     
     
     
    
     
]


    


