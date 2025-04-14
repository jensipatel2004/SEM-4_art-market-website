from django.urls import path
from . import views

urlpatterns = [
    path('',views.art_FSD, name='art_FSD'),
    path('artist/', views.artist, name="artist"),
	path('artwork/', views.artwork, name="artwork"),
    path('store/', views.store, name="store"),
    path('currentEvent/', views.currentEvent, name="currentEvent"),
    path('pastEvent/', views.pastEvent, name="pastEvent"),
    path('upcomingEvent/', views.upcomingEvent, name="upcomingEvent"),
    path('contact/', views.contact, name="contact"),
    path('signin/', views.user_login, name="login"),
    path('signout/', views.user_logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('update_item/',views.updateItem, name='update_item'),
    path('process_order/',views.processOrder, name='process_order'),
]
