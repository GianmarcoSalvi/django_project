from django.urls import path, include
from .views import city, region, poi, poi_opening_hour, province, user_account, image, tag, social_media, day_and_hour
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'region', region.RegionViewSet, basename='region') # 1
router.register(r'province', province.ProvinceViewSet, basename='province') # 2
router.register(r'city', city.CityViewSet, basename='city') # 3
router.register(r'user_account', user_account.UserAccountViewSet, basename='user_account') # 4
router.register(r'image', image.ImageViewSet, basename='image') # 5
router.register(r'tag', tag.TagViewSet, basename='tag') # 6
router.register(r'poi', poi.PoiViewSet, basename='poi') # 7
router.register(r'poi_opening_hour', poi_opening_hour.PoiOpeningHourViewSet, basename='poi_opening_hour') # 8
router.register(r'social_media', social_media.SocialMediaViewSet, basename='social_media') # 9
router.register(r'day_and_hour', day_and_hour.DayAndHourViewSet, basename='day_and_hour') # 10



urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    #path('region', views.region),
    #path('region/<str:pk>', views.region_id),
]