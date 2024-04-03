from django.contrib import admin
from django.urls import path, include
from .views import home,about,services,product, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path("about/",about,name='about'),
    path("services/", services, name='services'),
    path("contact/", ContactView.as_view(), name="contact"),
    path("product/", product, name = 'product'),
    
]