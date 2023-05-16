from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Farmapp import views
from django.conf.urls.static import static
from django.conf import settings 
router = routers.DefaultRouter()
router.register(r'products', views.ProductView, 'Farmapp')
router.register(r'categories', views.CategoryView, 'Farmapp')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
  
]

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )