import random
import abc

from itertools import chain
from typing import List, Optional, Iterable
from common.ngram import NgramCounter, extract_ngrams
from common.constants import SOS, EOS


class NgramModel(abc.ABC):
    def __init__(self, corpus, n):
        if n < 1:
            raise ValueError("`n` must be at least 1.")
        self.n = n
        self.vocab = list(set(chain(*corpus)) | {SOS, EOS})

    @classmethod
    def count_ngrams(cls, corpus: List[List[str]], n: int, m: Optional[int] = None) -> NgramCounter:
        ngrams = [ngram for sent in corpus for ngram in extract_ngrams(sent, n, m)]
        counts = NgramCounter(ngrams)
        return counts

    @abc.abstractmethod
    def proba(self, word: str, context: List[str]):
        pass

    def predict_next(self, context: List[str]) -> str:
        weights = [self.proba(w, context) for w in self.vocab]
        return random.choices(self.vocab, weights=weights, k=1)[0]

    def generate(self, start: Optional[Iterable[str]] = None, n_words: Optional[int] = None, max_words: int = 1000):
        if start is None:
            # Create empty context
            start = [SOS] * (self.n - 1)
        start = list(start)
        if len(start) < self.n - 1:
            start = [SOS] * (self.n - 1 - len(start)) + start
        generated = [*start]
        n_generated = 0
        # Fail-safe in case no <eos> is generated
        if n_words is not None:
            max_words = n_words
        while True:
            token = self.predict_next(generated[-self.n+1:])
            generated.append(token)
            n_generated += 1
            if (n_words is not None and n_generated >= n_words) or n_generated > max_words:
                return generated
            if token == EOS:
                if n_words is None:
                    # Halt when the first <eos> tag is encountered
                    return generated
                else:
                    # Keep generating words until reaching `n_words`
                    generated.extend([SOS] * (self.n - 1))
