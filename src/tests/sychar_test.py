"""Sychar unit tests."""

import pytest

from .. import sychar


def test_loading_a_bible_translation_file(tmp_path):
    dataset_dir = tmp_path / "datasets"
    dataset_dir.mkdir()
    test_translation_file = dataset_dir / "test_kjv.json"
    translation_contents = (
        '{"chapter":1,"verse":1,"text":"In the beginning God created the heaven and the earth."'
        ',"translation_id":"KJV","book_id":"Gen","book_name":"Genesis"}'
    )
    test_translation_file.write_text(translation_contents)
    expected_translation_dict = {
        "Genesis": {1: {1: "In the beginning God created the heaven and the earth."}}
    }
    assert (
        sychar.load_bible_translation(test_translation_file) == expected_translation_dict
    )
