"""project URL Configuration

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
from PedidosHoy.views import (index, PlatilloList, PlatilloMineList, 
                                PlatilloUpdate, PlatilloDelete, PlatilloCreate, Login, Logout, SignUp)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('platillo/list', PlatilloList.as_view(), name="platillo-list"),
    path('platillo/list', PlatilloMineList.as_view(), name="platillo-mine"),
    path('platillo/<pk>/update', PlatilloUpdate.as_view(), name="platillo-update"),
    path('platillo/<pk>/delete', PlatilloDelete.as_view(), name="platillo-delete"),
    path('platillo/create', PlatilloCreate.as_view(), name="platillo-create"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('signup/', SignUp.as_view(), name="signup"),
]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
