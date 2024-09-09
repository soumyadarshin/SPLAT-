"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from viewer import views 
from viewer.views import map_view,view_file_content
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.map_view, name='map_view'),
    path('download/<str:filename>/', views.download_report, name='download_report'),
    path('download/<str:filename>/', views.download_path_analysis, name='download_path_analysis'),
    path('view/<str:filename>/',views.view_file_content, name='view_file_content'),
    path('transmitter_data/',views.transmitter_data,name="transmitter_data"),
    path('receiver_data/',views.receiver_data,name="receiver_data"),
    path('run_splat_endpoint/', views.run_splat_endpoint, name='run_splat_endpoint'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
