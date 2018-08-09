Font Awesome and Markdown, together!
####################################

For when words aren't enough.
-----------------------------

.. image:: https://travis-ci.org/bmcorser/fontawesome-markdown.svg?branch=0.2.4
    :target: https://travis-ci.org/bmcorser/fontawesome-markdown

A Markdown extension that looks for things like ``:fa-coffee:`` and replaces
them with the Font Awesome icon markup.

Add ``'fontawesome_markdown'`` to your Markdown call and watch the
magic unfold:

.. code-block:: python

    >>> from markdown import Markdown

    >>> markdown = Markdown(extensions=['fontawesome_markdown']
    >>> markdown.convert('i ♥ :fa-coffee:')
    <p>i ♥ <i class="fa fa-coffee"></i></p>

    >>> markdown.convert('i ♥ :far fa-fontawesome: fa-x3')
    <p>i ♥ <i class="far fa-coffee fa-x3"></i></p>


Don't forget to make the Font Awesome v5.2 assets available to your DOM, and you're done!

Issue
========

* light prefix is not support now.(I can not found metadata)