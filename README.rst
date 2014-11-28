Font Awesome and Markdown, together!
####################################
For when words aren't enough.
-----------------------------

A Markdown extension that looks for things like ``:fa-coffee:`` and replaces
them with the Font Awesome icon markup.

Add a ``FontAwesomeExtension`` instance to your Markdown call and watch the
magic unfold::

    >>> from markdown import Markdown
    >>> from fontawesome_markdown import FontAwesomeExtension

    >>> markdown = Markdown(extensions=[FontAwesomeExtension()]
    >>> markdown.convert('i ♥ :fa-coffee:')
    <p>i ♥ <i class="fa fa-coffee"></i></p>

Don't forget to make the Font Awesome assets available to your DOM, and you're done!

.. image:: https://travis-ci.org/bmcorser/fontawesome-markdown.svg
