from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from reviews.views import ReviewViewSet


app_name = 'reviews'

router = DefaultRouter()
router.register('review', ReviewViewSet, base_name='reviews')

urlpatterns = [
    url(r'reviews/', include(router.urls))
]
