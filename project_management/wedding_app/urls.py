from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_items, name='category_items'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('view-orders/', views.view_orders, name='view_orders'),
    path('delete-item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('order-placed/', views.order_placed, name='order_placed'),
]
