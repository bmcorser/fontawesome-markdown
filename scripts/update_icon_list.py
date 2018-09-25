'Update the icon_list module from the FontAwesome GitHub repo'
import requests
import json
import itertools
import pprint

URI = ('https://raw.githubusercontent.com'
       '/FortAwesome/Font-Awesome/master/advanced-options/metadata/icons.json')


def main():
    icons_json = requests.get(URI).json()
    # use only styles
    icons = {
        icon_name: tuple(icons_json[icon_name]['styles'])
        for icon_name in icons_json.keys()
    }
    with open('../fontawesome_markdown/icon_list.py', 'w') as icons_list_py:
        icons_list_py.write('from __future__ import unicode_literals\n')
        icons_list_py.write('icons = ')
        icons_list_py.write(json.dumps(icons, indent=2))
if __name__ == '__main__':
    main()
