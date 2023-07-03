from web.core.models import Deck
from typing import Dict


class DeckCreator():
    def create_deck(self, deck_type, *args, **kwargs) -> Dict["Deck", Deck]:
        res = {}
        deck_inst = Deck(deck_type=deck_type)
        deck_inst.save()
        res[f"{deck_inst}"] = deck_inst
        return res