
from rest_framework.routers import DefaultRouter
from .views import PessoasViewSet

router = DefaultRouter()
router.register(r'pessoas', PessoasViewSet, basename='pessoas')

urlpatterns = router.urls
