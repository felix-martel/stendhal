import os
from epub_conversion.utils import open_book, convert_epub_to_lines
from bs4 import BeautifulSoup
from typing import Union


def _read_epub(path: Union[str, os.PathLike]) -> str:
    book = open_book(path)
    raw = "\n".join(convert_epub_to_lines(book))
    return raw


def from_epub(path: Union[str, os.PathLike]) -> str:
    raw = _read_epub(path)
    parsed = BeautifulSoup(raw, "html.parser")
    content = [paragraph.get_text() for paragraph in parsed.find_all("p")]
    # corpus = re.sub("(\n)+", "\\n", corpus)
    return "".join(content)