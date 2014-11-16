# coding: utf-8
from __future__ import unicode_literals
import pytest
from markdown import Markdown
from fontawesome_markdown import FontAwesomeExtension, FontAwesomeException


@pytest.fixture
def fa_markdown():
    return Markdown(extensions=[FontAwesomeExtension()])


def test_example(fa_markdown):
    assert fa_markdown.convert('i ♥ :fa-coffee:') == '<p>i ♥ <i class="fa fa-coffee"></i></p>'

def test_unknown_raises(fa_markdown):
    unknown_icon = 'arglebargle'
    with pytest.raises(FontAwesomeException) as exc:
        fa_markdown.convert("i ♥ :fa-{0}:".format(unknown_icon))
        assert unknown_icon in exc.message
