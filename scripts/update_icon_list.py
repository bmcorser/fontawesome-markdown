'Update the icon_list module from the FontAwesome GitHub repo'
import requests
import yaml
import itertools
import pprint

URI = ('https://raw.githubusercontent.com'
       '/FortAwesome/Font-Awesome/master/src/icons.yml')


def main():
    icons_list = yaml.load(requests.get(URI).text)['icons']
    names_aliases = lambda I: itertools.chain([I['id']], I.get('aliases', list()))
    names = tuple(itertools.chain(*map(names_aliases, icons_list)))
    with open('../fontawesome_markdown/icon_list.py', 'w') as icons_list_py:
        icons_list_py.write('from __future__ import unicode_literals\n')
        icons_list_py.write('icons = \\\n')
        pprint.pprint(names, icons_list_py)

if __name__ == '__main__':
    main()
