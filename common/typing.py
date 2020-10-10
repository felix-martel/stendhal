from typing import List, Optional, Iterable, Union, Tuple, Counter

Ngram = Tuple[str]
NgramCounter = Counter[Ngram]

SegmentizedCorpus = List[str]
TokenizedSentence = List[str]
TokenizedCorpus = List[TokenizedSentence]