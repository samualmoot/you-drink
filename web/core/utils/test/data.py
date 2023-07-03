from web.core.models import Deck
from typing import Dict


class DeckCreator():
    def create_deck(self, deck_type, *args, **kwargs) -> Deck:
        
        deck_inst = Deck(deck_type=deck_type)
        deck_inst.save()
        
        return deck_inst