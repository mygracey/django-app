from django.urls import path
from . import views


urlpatterns = [
    path('',views.indexPage,name='index'),
    path('register/',views.registerPage,name='register'),
    path('products/',views.productsPage,name='products'),
    path('logout/',views.logoutPage,name='logout'),
]
