from web.core.models import Deck, Card
from typing import Dict


class DeckCreator():
    def create_deck(self, deck_type, name, *args, **kwargs) -> Deck:
        
        deck_inst = Deck(type=deck_type, name=name)
        deck_inst.save()
        
        return deck_inst
    
class CardCreator():
    def create_card(self, message, drink_amount, deck):
        card_inst = Card(message=message, drink_amount=drink_amount, deck=deck)
        card_inst.save()