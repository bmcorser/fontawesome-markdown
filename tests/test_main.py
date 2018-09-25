# coding: utf-8
from __future__ import unicode_literals
import pytest
from markdown import Markdown
from fontawesome_markdown import FontAwesomeExtension, FontAwesomeException


@pytest.fixture(params=[FontAwesomeExtension(), 'fontawesome_markdown'], ids=["import", "string"])
def fa_markdown(request):
    return Markdown(extensions=[request.param])


def test_example(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa fa-coffee"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-coffee:') == expected_markup


def test_unknown_raises(fa_markdown):
    unknown_icon = 'arglebargle'
    with pytest.raises(FontAwesomeException, match=unknown_icon) as exc:
        fa_markdown.convert("i ♥ :fa-{0}:".format(unknown_icon))
        assert unknown_icon in exc.value.message


def test_prefix_not_found_raises(fa_markdown):
    with pytest.raises(FontAwesomeException, match="prefix 'fa' is not found in facebook"):
        fa_markdown.convert("i ♥ :fa fa-facebook:")
    

def test_size(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa fa-coffee fa-xs"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-coffee fa-xs:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa fa-coffee fa-sm"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-coffee fa-sm:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa fa-coffee fa-lg"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-coffee fa-lg:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa fa-coffee fa-1x"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-coffee fa-1x:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa fa-coffee fa-3x"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-coffee fa-3x:') == expected_markup

    expected_markup = '<p>i ♥ <i class="fa fa-coffee fa-10x"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-coffee fa-10x:') == expected_markup


def test_fab_icon(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fab fa-facebook"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-facebook:') == expected_markup


def test_fab_icon_with_prefix(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fab fa-facebook"></i></p>'
    assert fa_markdown.convert('i ♥ :fab fa-facebook:') == expected_markup


def test_far_icon_with_prefix(fa_markdown):
    expected_markup = '<p>i ♥ <i class="far fa-font-awesome-logo-full"></i></p>'
    assert fa_markdown.convert('i ♥ :far fa-font-awesome-logo-full:') == expected_markup


def test_fa_icon_without_prefix(fa_markdown):
    expected_markup = '<p>i ♥ <i class="fa fa-font-awesome-logo-full"></i></p>'
    assert fa_markdown.convert('i ♥ :fa-font-awesome-logo-full:') == expected_markup


# light style not found in icons.json...
# def test_fal_icon_with_prefix(fa_markdown):
    # expected_markup = '<p>i ♥ <i class="fal fa-font-awesome-logo-full"></i></p>'
    # assert fa_markdown.convert('i ♥ :fal fa-font-awesome-logo-full:') == expected_markup