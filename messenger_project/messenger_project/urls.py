from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from chat import views

router = routers.DefaultRouter()
router.register(r'rooms', views.RoomViewset, basename='rooms')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-v1/', include(router.urls), name='api'),
    path('chat/', include('chat.urls'), ),
    path('', include('chat.urls'), ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]