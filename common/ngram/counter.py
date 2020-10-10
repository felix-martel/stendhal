from collections import Counter, defaultdict
import typing as ty
from .typing import Ngram, NgramLike, RawNgramCounter


class NgramCounter(object):
    def __init__(self, ngrams: ty.Iterable[NgramLike] = None, auto_lower_order: bool = False):
        self._counts = defaultdict(Counter)
        self.lower_order = auto_lower_order
        if ngrams is not None:
            for ngram in ngrams:
                self[ngram] += 1

    def extend(self, ngrams: ty.Iterable[NgramLike]) -> None:
        for ngram in ngrams:
            self[ngram] += 1

    def items(self):
        yield from self._counts.items()

    def __setitem__(self, ngram: NgramLike, count: int) -> None:
        ngram = tuple(ngram)
        n = len(ngram)
        self._counts[n][ngram] = count

    def __getitem__(self, ngram_or_subcount: ty.Union[NgramLike, int]) -> ty.Union[RawNgramCounter, int]:
        if isinstance(ngram_or_subcount, int):
            n = ngram_or_subcount
            return self._counts[n]
        ngram = tuple(ngram_or_subcount)
        n = len(ngram)
        return self._counts[n][ngram]

    def __contains__(self, ngram: NgramLike) -> bool:
        ngram = tuple(ngram)
        n = len(ngram)
        return n in self._counts and ngram in self._counts[n]

