# coding: utf-8
from __future__ import unicode_literals
import pytest
from markdown import Markdown
from fontawesome_in_markdown import FontAwesomeInlineProcessor, FontAwesomeException, FontAwesomeExtension

@pytest.fixture(params=[
    FontAwesomeExtension(),
    'fontawesome_in_markdown'
], ids=["import", "string"])
def fa_markdown(request):
    return Markdown(extensions=[request.param])


def test_example(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot:') == expected_markup


def test_unknown_raises(fa_markdown):
    unknown_icon = 'arglebargle'
    with pytest.raises(FontAwesomeException, match=unknown_icon) as exc:
        fa_markdown.convert("i ♥ :fa-{0}:".format(unknown_icon))
        assert unknown_icon in exc.value.message


def test_prefix_not_found_raises(fa_markdown):
    with pytest.raises(FontAwesomeException, match="Prefix 'prefix' is not available for facebook."):
        fa_markdown.convert("i ♥ :fa fa-facebook:")
    

def test_size(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot fa-xs"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot fa-xs:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot fa-sm"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot fa-sm:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot fa-lg"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot fa-lg:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot fa-1x"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot fa-1x:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot fa-3x"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot fa-3x:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa-solid fa-mug-hot fa-10x"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-mug-hot fa-10x:') == expected_markup


def test_fab_icon(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-brands fa-facebook"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-facebook:') == expected_markup


def test_fab_icon_with_prefix(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-brands fa-facebook"></i></p>'
    assert fa_markdown.convert('i ♥ :fab fa-facebook:') == expected_markup


def test_far_icon_with_prefix(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-regular fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :far fa-star:') == expected_markup


def test_fa_icon_without_prefix(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa-solid fa-star"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-star:') == expected_markup


# light style not found in icons.json...
# def test_fal_icon_with_prefix(fa_markdown):
    # expected_markup = '<p>i ♥ <i class="fal fa-font-awesome-logo-full"></i></p>'
    # assert fa_markdown.convert('i ♥ :fal fa-font-awesome-logo-full:') == expected_markup