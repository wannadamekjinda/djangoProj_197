"""djangoProj_197 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ProfileApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('base', views.base, name='base'),
    path('resume', views.resume, name='resume'),
    path('educational',views.educational,name='educational'),
    path('interests',views.interests,name='interests'),
    path('occupaton',views.occupation,name='occupation'),
    path('roleModel',views.roleModel,name='roleModel'),
    path('sale',views.sale,name='sale'),
    path('earphone',views.earphone,name='earphone'),
    path('keyboard',views.keyboard,name='keyboard'),
    path('speaker',views.speaker,name='speaker'),
    path('showData',views.showData,name='showData'),
]


