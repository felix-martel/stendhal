from typing import Optional, List

from common.typing import TokenizedCorpus
from .lidstone import Lidstone


class Laplace(Lidstone):
    def __init__(self, corpus : TokenizedCorpus, n : int, vocab : Optional[List[str]] = None):
        super().__init__(corpus, n, vocab, gamma=1.0)