from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree
from .icon_list import icons
from .styleutil import prefix_to_style, style_to_prefix
import json

fontawesome_pattern = r':(fa[bsrl]?)?\s?fa-([-\w]+):'


class FontAwesomeException(Exception):
    'Exception for unknown icon names'
    pass


class FontAwesomePattern(Pattern):
    'Markdown pattern class for matching things that look like FA icons'
    def handleMatch(self, m):
        el = etree.Element('i')
        prefix = m.group(2)
        icon_name = m.group(3)
        test = m.group(1)
        if icon_name in icons:
            styles = icons[icon_name]
            if not prefix and 'solid' in styles:
                # default prefix is fa
                prefix = 'fa'
            elif not prefix and 'solid' not in styles:
                style = styles[0]
                prefix = style_to_prefix(style)
                if not prefix:
                    raise FontAwesomeException("unknown style {0}".format(style))
            
            elif prefix and prefix_to_style(prefix) not in styles:
                raise FontAwesomeException("{0} have not prefix '{1}'.\nAllowed prefix is {2} ".format(icon_name, prefix, styles))
            
            
            el.attrib = {'class': '{0} fa-{1}'.format(prefix, icon_name)}
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