"""Button URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.responseform_tweezer),
    path('', views.responseform_splint),
    path('submitted1/', views.responseform_tweezer),
    path('submitted2/', views.responseform_splint),
    path('submitted3/', views.responseform_clips),
    path('general/', views.general,name='GHC'),
    path('tweezers/', views.responseform_tweezer,name='tweezers'),
    path('splints/', views.responseform_splint,name='splints'),
    path('clips/', views.responseform_clips,name='clips'),
    #path('clips/', views.responseform,name='clips'),
    #path('output', views.output,name="script"),
    
  
]
