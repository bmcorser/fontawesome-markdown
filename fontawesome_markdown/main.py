from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
import xml.etree.ElementTree as etree
from .icon_list import icons
import json

fontawesome_pattern = r':(fa[bsrl]?)?\s?fa-([-\w]+)\s?(fa-(xs|sm|lg|[\d+]x|10x))?:'

prefix_to_style = {
    'fas': 'solid',
    'fa': 'solid',
    'fab': 'brands',
    'far': 'regular',
    'fal': 'light',
}

style_to_prefix = {v: k for k, v in prefix_to_style.items()}


class FontAwesomeException(Exception):
    'Exception for unknown icon name, prefix or size'
    pass


class FontAwesomePattern(InlineProcessor):
    'Markdown pattern class for matching things that look like FA icons'

    def handleMatch(self, match, data):
        el = etree.Element('i')
        prefix = match.group(1)
        icon_name = match.group(2)
        size = match.group(3)
        if icon_name in icons:
            styles = icons[icon_name]
            if not prefix and 'solid' in styles:
                # default prefix is fa
                prefix = 'fa'
            elif not prefix and 'solid' not in styles:
                style = styles[0]
                prefix = style_to_prefix.get(style)
                if not prefix:
                    message = "unknown style {0}".format(style)
                    raise FontAwesomeException(message)

            elif prefix and prefix_to_style.get(prefix) not in styles:
                message = "prefix '{0}' is not found in {1}.\n Allowed prefix is {2} ".format(prefix, icon_name, styles)

                raise FontAwesomeException(message)

            css_class = '{0} fa-{1}'.format(prefix, icon_name)
            if size:
                css_class += " " + size
            el.attrib = {'class': css_class}
            return el, match.start(0), match.end(0)
        message = "{0} isn't a FA icon I know about".format(icon_name)
        raise FontAwesomeException(message)


class FontAwesomeExtension(Extension):
    'Pick a good spot for calling the pattern defined above'

    def extendMarkdown(self, md):
        fontawesome = FontAwesomePattern(fontawesome_pattern)
        md.inlinePatterns.register(fontawesome, 'fontawesome', 175)


def makeExtension(*args, **kwargs):
    return FontAwesomeExtension(*args, **kwargs)
