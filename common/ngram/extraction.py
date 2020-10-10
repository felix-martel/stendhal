from typing import List, Generator, Optional
from .typing import Ngram
from ..constants import SOS, EOS


def extract_ngrams(sentence: List[str], n: int, m: Optional[int] = None) -> List[Ngram]:
    """
    both bounds are inclusive
    :param sentence:
    :param n:
    :param m:
    :return:
    """
    if m is None:
        m = n
    if n > m:
        raise ValueError(f"The lowest order `n` must be lesser than the highest order `m` (found `n`={n}, `m`={m})")
    pad_size = max(1, m-1)
    padded = [SOS] * pad_size + sentence + [EOS] * pad_size
    ngrams = [tuple(padded[i:i+k]) for k in range(n, m+1) for i in range(len(padded)-k)]
    return ngrams


def enumerate_subgrams(ngram: Ngram) -> Generator[Ngram, None, None]:
    while ngram:
        ngram = ngram[1:]
        yield ngram
