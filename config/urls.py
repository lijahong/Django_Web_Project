"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import board.views
import product.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.mainPage), #메인페이지로 url이 입력되지 않은 상태
    path('product/create', product.views.createFruitGet),
    path('product/createPost', product.views.createFruitPost),
    path('product/getlist', product.views.readFruitGet),
    path('board/getdata', board.views.createBoardGet),
    path('board/postdata', board.views.createBoardPost),
    path('board/readdata', board.views.createReadBoard),
]