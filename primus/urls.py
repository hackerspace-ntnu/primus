from django.conf.urls import url, include
from primus import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'contests', views.ContestViewSet, base_name='contest')

urlpatterns = [
    url(r'^', include(router.urls))
]