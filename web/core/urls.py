from web.core.api.v1.views.deck import DeckViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'deck', DeckViewSet, basename='api/core/v1/deck')
urlpatterns = router.urls
