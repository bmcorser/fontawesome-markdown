from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree

fontawesome_pattern = r':(fa-[-\w]+):'

class FontAwesomePattern(Pattern):
    def handleMatch(self, m):
        el = etree.Element('i')
        icon_name = m.group(2)
        el.set('class', 'fa ' + icon_name)
        return el

class FontAwesomeExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        fontawesome = FontAwesomePattern(fontawesome_pattern)
        md.inlinePatterns.add('fontawesome', fontawesome, '<reference')
