from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree
from icon_list import icons

fontawesome_pattern = r':(icon-[-\w]+):'

class FontAwesomePattern(Pattern):
    def handleMatch(self, m):
        el = etree.Element('i')
        icon_name = m.group(2)
        if icon_name in icons:
            el.attrib = {'class':'fa {0}'.format(icon_name)}
            return el
        return m.string

class FontAwesomeExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        fontawesome = FontAwesomePattern(fontawesome_pattern)
        md.inlinePatterns.add('fontawesome', fontawesome, '<reference')
