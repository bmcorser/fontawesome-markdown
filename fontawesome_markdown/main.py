from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree
from .icon_list import icons

fontawesome_pattern = r':fa-([-\w]+):'


class FontAwesomeException(Exception):
    'Exception for unknown icon names'
    pass


class FontAwesomePattern(Pattern):
    'Markdown pattern class for matching things that look like FA icons'
    def handleMatch(self, m):
        el = etree.Element('i')
        icon_name = m.group(2)
        if icon_name in icons:
            el.attrib = {'class': 'fa fa-{0}'.format(icon_name)}
            return el
        message = "{0} isn't a FA icon I know about".format(icon_name)
        raise FontAwesomeException(message)


class FontAwesomeExtension(Extension):
    'Pick a good spot for calling the pattern defined above'
    def extendMarkdown(self, md, md_globals):
        fontawesome = FontAwesomePattern(fontawesome_pattern)
        md.inlinePatterns.add('fontawesome', fontawesome, '<reference')


def makeExtension(*args, **kwargs):
    return FontAwesomeExtension(*args, **kwargs)