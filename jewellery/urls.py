"""jewellery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from firstapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),  
    path('index.html', views.index,name="home"),
    path('gallery.html/',views.gallery,name="gallery"),
     path('about.html/',views.about,name="about"),
      path('contact.html/',views.contact,name="contact"), 
      path('registration.html/',views.registration,name="registration"),
      path('login.html/',views.login,name="login") ,
      path('show.html/',views.show,name="show"),
       path('show1.html/',views.show1,name="show1"),
        path('show2.html/',views.show2,name="show2"),
        path('show3.html/',views.show3,name="show3"),
       path('new.html/',views.new,name="new"),
       path('new1.html/',views.new1,name="new1"),
        path('new2.html/',views.new2,name="new2"),
         path('new3.html/',views.new3,name="new3"),
          path('new4.html/',views.new4,name="new4")
       
       
]
