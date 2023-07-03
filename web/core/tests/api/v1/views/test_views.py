from django.test import TestCase
from web.core.api.v1.views.deck import DeckViewSet
from typing import ClassVar, List, Optional, Any
from web.core.utils.test.data import DeckCreator

# Create your tests here.
class DeckViewSetTest(TestCase):
    named_view_base: ClassVar[str] = "api/core/v1/deck"
    namespace: ClassVar[str] = None
    viewset: DeckViewSet

    FIELDS: ClassVar[List[str]] = [
        "deck_type"
    ]

    CREATOR_CLASS: ClassVar[Optional[Any]]

    @classmethod
    def setUp(cls) -> None:
        # Create a deck used for testing
        deck = DeckCreator().create_deck(deck_type=="test", name="test deck")
        cls.deck_type = deck.deck_type

    
    def test_list(self) -> None:
        pass

    def test_retrieve(self) -> None:
        pass