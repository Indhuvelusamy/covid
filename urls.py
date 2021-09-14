"""covid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('charts',views.charts,name="charts"),
    path('prediction',views.prediction,name="prediction"),
    #path('tamilnadu',views.tamilnadu,name="tamilnadu"),
    path('tamilnadu_prediction',views.tamilnadu_prediction,name="tamilnadu_prediction"),
    path('covidend',views.covidend,name="covidend"),
    path('district_wise',views.district_wise,name="district_wise"),
    path('state_wise',views.state_wise,name="state_wise"),
    path('admin/', admin.site.urls),
]
