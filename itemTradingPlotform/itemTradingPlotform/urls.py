"""itemTradingPlotform URL Configuration

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
from django.urls import path, include
from exchange import views  

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/',views.login),
    path('logout/',views.logout),
    path('register/',views.register),
    path('captcha/',include('captcha.urls')),

    path('publish/me/',views.publish_me),
    path('publish/',views.publish), 

    path('receive/<int:rid>/',views.receive_requirement),
    path('receive/list/',views.receive_list),
    path('receive/me/',views.receive_me),
    
    
    path('delete/<int:rid>/',views.concel_requirement),
    
    path('finish/<int:rid>/',views.finish_requirement),
    path('abandon/<int:rid>/',views.abandon_requirement),
    path('info/edit/',views.info_edit),
]
