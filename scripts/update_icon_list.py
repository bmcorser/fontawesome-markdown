'Update the icon_list module from the FontAwesome GitHub repo'
import requests
import yaml
import itertools
import pprint

URI = ('https://raw.githubusercontent.com'
       '/FortAwesome/Font-Awesome/master/src/icons.yml')

def main():
    icons_list = yaml.load(requests.get(URI).text)['icons']
    name_aliases = lambda I: itertools.chain([I['id']], I.get('aliases', list()))
    names_list = tuple(itertools.chain(*map(name_aliases, icons_list)))
    with open('../fontawesome_markdown/icon_list.py', 'w') as icons_list_py:
        icons_list_py.write('icons = \\\n')
        pprint.pprint(map(lambda N: 'fa-' + N, names_list), icons_list_py)
    with open('../fontawesome_markdown/icon_list.py', 'r') as icons_list_py:
        print(icons_list_py.read())

if __name__ == '__main__':
    main()
