import random
from collections import Counter
from typing import List, Optional

from common.typing import TokenizedCorpus
from .abc import NgramModel
from common.ngram import NgramCounter, NgramLike
from .mle import MLE


class GoodTuring(MLE):
    def __init__(self, corpus : TokenizedCorpus, n : int, vocab : Optional[List[str]] = None, stop_discounting_at=4):
        super().__init__(corpus, n, vocab)
        self.smoothed = self.smooth_counts(self.counts, stop_discounting_at)

    def smooth_counts(self, raw_counts: NgramCounter, stop_discounting: int = 4):
        # count_of_counts = {n: Counter(counts.values()) for n, counts in raw_counts.items()}
        smoothed_counts = dict()
        for n, counts in raw_counts.items():
            count_of_counts = Counter(counts.values())
            count_of_counts[0] = len(self.vocab)**n - len(counts)
            last_discounted_index = min(i for i, c in count_of_counts.items() if c <= stop_discounting)
            new_counts = dict()
            for r in range(0, last_discounted_index-1):
                r_star = (r + 1) * count_of_counts[r + 1] / count_of_counts[r]
                new_counts[r] = r_star
            smoothed_counts[n] = new_counts
        return smoothed_counts

    def get_count(self, ngram: NgramLike) -> float:
        ngram = tuple(ngram)
        n = len(ngram)
        r = self.counts[ngram]
        if n not in self.smoothed:
            return r
        r_star = self.smoothed[n].get(r, r)
        return r_star

    def proba(self, word: str, context: List[str]) -> float:
        p_context = self.get_count(context)
        if p_context:
            p_word = self.get_count((*context, word))
            return p_word / p_context
        return 0.0
