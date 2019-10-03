from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from rest_framework import routers

from Main.views import UrlObjectViewSet

router = routers.DefaultRouter()
router.register(r'api/fetcher', UrlObjectViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
