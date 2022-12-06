from rest_framework import routers
from .views import ProductViewSet, CouponViewSet, OrderItemViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'coupon', CouponViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderitem', OrderItemViewSet)

urlpatterns = router.urls
