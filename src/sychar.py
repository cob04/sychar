""" Sychar. Read Bible verses from translation JSON datasets

Usage:
>>> python3 sychar.py --help

>>> python3 sychar.py --book Isaiah --chapter 1 --verse 18
"""
#!/usr/bin/env python3

import argparse
import json
from typing import Tuple


def load_bible_translation(dataset_file: str) -> dict:
    """read the translation JSON dataset and load it into a dictionary.

    load the json data into a dictinary with a key for every book, a nested
    dictionary for every chapter containing a nested dictionary for each verse.
    e.g.

    {"Genesis": {1: {1: "In the begining.."},...}}

    Args:
        dataset_file (str): path to a bible translation dataset json file.
    Returns:
        dict: a dictionary of nested dictionaries of books, chapters and verses.
    """
    translation: dict = {}
    with open(dataset_file, "rt") as f:
        lines = [json.loads(line.strip()) for line in f.readlines()]

    for line in lines:
        book, chapter, verse, text = (
            line["book_name"],
            line["chapter"],
            line["verse"],
            line["text"],
        )
        if not translation.get(book):
            translation[book] = {}
        if not translation[book].get(chapter):
            translation[book][chapter] = {}
        if not translation[book][chapter].get(verse):
            translation[book][chapter][verse] = text
    return translation


def read_bible_verse(translation: dict, verse_selection: Tuple[str, str, str]) -> Tuple[str, str, str]:
    """Return a Bible verse text along with the book, chapter, and verse details.

    Args:
        translation (dict): a dictionary of nested dictionaries for books, chapters, and verses.
        verse_selection (tuple): a tuple containing the book, chapter, and verse (e.g., ('Genesis', 1, 1))

    Returns:
        tuple: A tuple containing the book, chapter, verse, and text for the selected verse.
    """
    book, chapter, verse = verse_selection
    text = translation[book][chapter][verse]
    return book, chapter, verse, text


def get_args():
    parser = argparse.ArgumentParser(
        description="Read Bible verses from translation JSON datasets"
    )
    parser.add_argument("-b", "--book", required=True)
    parser.add_argument("-c", "--chapter", type=int, required=True)
    parser.add_argument("-v", "--verse", type=int, required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    translation = load_bible_translation("../datasets/kjv.json")
    verse_selection = (args.book, args.chapter, args.verse)
    book, chapter, verse, text = read_bible_verse(translation, verse_selection)

    verse_reference = f"{book} {chapter}:{verse} (KJV)"
    print(f"{verse_reference}")
    print(f"{text}")





