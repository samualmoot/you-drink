from django.test import TestCase
from web.core.api.v1.views.deck import DeckViewSet
from typing import ClassVar, List, Optional, Any, Dict 
from web.core.utils.test.data import DeckCreator, CardCreator
from web.models import Card, Deck

# Create your tests here.
class DeckViewSetTest(TestCase):
    named_view_base: ClassVar[str] = "api/core/v1/deck"
    namespace: ClassVar[str] = None
    viewset: DeckViewSet

    FIELDS: ClassVar[List[str]] = [
        "name",
        "type"
    ]

    CREATOR_CLASS: ClassVar[Optional[Any]]

    @classmethod
    def setUp(cls) -> None:
        # Create a deck used for testing
        cls.deck = DeckCreator().create_deck(deck_type=="test", name="test deck")

    
    def test_list(self) -> None:
        pass

    def test_retrieve(self) -> None:
        pass


class CardViewSetTest(TestCase):
    named_view_base: ClassVar[str] = "api/core/v1/card"
    namespace: ClassVar[str] = None
    viewset: DeckViewSet

    FIELDS: ClassVar[List[str]] = [
        "message",
        "type",
        "drink_amount",
        "deck"
    ]

    @classmethod
    def setUp(cls) -> None:
        # Create a deck used for testing
        cls.deck = DeckCreator().create_deck(deck_type="test", name="test deck")
        cls.cards: Dict[int, Card] = CardCreator().create_card(message="test message", drink_amount=2, deck=cls.deck, type="test", count=3)
        
    
    def test_list(self) -> None:
        pass

    def test_retrieve(self) -> None:
        pass

