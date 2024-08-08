from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('profile/', views.profile, name="profile"),

    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    # category
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),

    # login urls
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),

    # Cart URLs
    path('cart/', views.cart_item, name='cart'),
    # path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),

    # Review URLs
    path('products/<int:product_pk>/review/', views.review_create, name='review_create'),
]
