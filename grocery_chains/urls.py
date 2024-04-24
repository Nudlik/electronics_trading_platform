from django.urls import include, path
from rest_framework.routers import DefaultRouter

from grocery_chains import apps
from grocery_chains.views import GroceryChainViewSet

app_name = apps.GroceryChainConfig.name

router = DefaultRouter()
router.register('chains', GroceryChainViewSet, basename='chains')

urlpatterns = [
    path('', include(router.urls)),
]
