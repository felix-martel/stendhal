from typing import List
import re


SegmentizedCorpus = List[str]
TokenizedSentence = List[str]
TokenizedCorpus = List[TokenizedSentence]


def clean(corpus: str) -> str:
    return corpus.lower().replace("\n", " ")


def segmentize(corpus: str) -> SegmentizedCorpus:
    return re.split("[.!?]", corpus)


def tokenize_one(sentence: str) -> TokenizedSentence:
    return [w for w in re.split("\W+", sentence) if w]


def tokenize(sentences: List[str]) -> TokenizedCorpus:
    return [tokenize_one(sentence) for sentence in sentences]


def preprocess_one(sentence: str) -> TokenizedSentence:
    return tokenize_one(clean(sentence))


def preprocess(corpus: str) -> TokenizedCorpus:
    return tokenize([s for s in segmentize(clean(corpus)) if s])
