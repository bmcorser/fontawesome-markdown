def prefix_to_style(prefix):
    if prefix in ('fas', 'fa'):
        return 'solid'
    elif prefix == 'fab':
        return 'brands'
    elif prefix == 'far':
        return 'regular'
    elif prefix == 'fal':
        return 'light'
    else:
        return None

def style_to_prefix(style):
    if style == 'brands':
        return 'fab'
    elif style == 'regular':
        return 'far'
    elif style == 'light':
        return 'fal'
    elif style == 'solid':
        return 'fa'
    else:
        return None