"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from payment.views import go_to_gateway_view

from azbankgateways.urls import az_bank_gateways_urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls',namespace='home')),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('go-to-gateway/', go_to_gateway_view),
    path("bankgateways/", az_bank_gateways_urls()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
