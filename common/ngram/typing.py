from typing import Tuple, Counter, Iterable

# Any iterable of str is an acceptable type for input ngrams...
NgramLike = Iterable[str]
# ...but all n-grams are casted to tuples internally (they need to be hashable)
Ngram = Tuple[str]
# A simple counter (`collections.Counter`) of n-grams
RawNgramCounter = Counter[Ngram]