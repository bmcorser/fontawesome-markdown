'Update the icon_list module from the FontAwesome GitHub repo'
import requests
import json
import pprint

URI = ('https://raw.githubusercontent.com'
       '/FortAwesome/Font-Awesome/6.x/metadata/icons.json')

def main():
    try:
        response = requests.get(URI)
        response.raise_for_status()
        icons_json = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return

    # use only styles
    icons = {
        icon_name: tuple(icons_json[icon_name]['styles'])
        for icon_name in icons_json.keys()
    }

    with open('../src/fontawesome_in_markdown/icon_list.py', 'w') as icons_list_py:
        icons_list_py.write('from __future__ import unicode_literals\n')
        icons_list_py.write('icons = ')
        icons_list_py.write(json.dumps(icons, indent=2))

if __name__ == '__main__':
    main()
