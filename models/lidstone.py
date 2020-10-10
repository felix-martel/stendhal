from .mle import MLE
from common.ngram import NgramLike


class Lidstone(MLE):
    def __init__(self, corpus, n, gamma: float = 1.):
        super().__init__(corpus, n)
        if self.gamma < 0:
            raise ValueError("For Lidstone or Laplace models, `gamma` must be positive. "
                             "It is usually chosen within (0, 1).")
        self.gamma = gamma

    def proba(self, word: str, context: NgramLike) -> float:
        if self.gamma == 0 and self.counts[context] == 0:
            return 0.0
        return (self.counts[(*context, word)] + self.gamma) / (self.counts[context] + self.gamma * len(self.vocab))
