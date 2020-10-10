import random
from typing import List

from .abc import NgramModel


class MLE(NgramModel):
    def __init__(self, corpus, n):
        super().__init__(corpus, n)
        self.counts = self.count_ngrams(corpus, self.n-1, self.n)

    def proba(self, word: str, context: List[str]):
        p_context = self.counts[context]
        if p_context:
            return self.counts[(*context, word)] / p_context
        return 0.0

    def predict_next(self, context: List[str]) -> str:
        if context not in self.counts:
            return random.choice(self.vocab)
        super().predict_next(context)
