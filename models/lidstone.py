from typing import Optional, List

from common.typing import TokenizedCorpus
from .mle import MLE
from common.ngram import NgramLike


class Lidstone(MLE):
    def __init__(self, corpus : TokenizedCorpus, n : int, vocab : Optional[List[str]] = None, gamma: float = 1.0):
        super().__init__(corpus, n, vocab)
        if gamma < 0:
            raise ValueError("For Lidstone or Laplace models, `gamma` must be positive. "
                             "It is usually chosen within (0, 1).")
        self.gamma = gamma

    def proba(self, word: str, context: NgramLike) -> float:
        if self.gamma == 0 and context not in self.counts:
            return 0.0
        return (self.counts[(*context, word)] + self.gamma) / (self.counts[context] + self.gamma * len(self.vocab))
