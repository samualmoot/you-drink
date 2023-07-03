from web.core.models import Deck, Card
from typing import Dict


class DeckCreator():
    def create_deck(self, deck_type: str, name: str, *args, **kwargs) -> Deck:
        deck_inst = Deck(type=deck_type, name=name)
        deck_inst.save()
        return deck_inst
    
class CardCreator():
    def create_card(self, card_type: str, message: str, drink_amount: int, deck: Deck, count: int = 1, *args, **kwargs) -> Dict:
        res = {}
        for x in range(count):
            card_inst = Card(message=message, drink_amount=drink_amount, deck=deck, type=card_type)
            card_inst.save()
            res[x] = card_inst
        return res