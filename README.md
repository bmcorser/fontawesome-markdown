## Easily place FontAwesome icons in your MarkDown files

This is a Markdown extension to include FontAwesome icons in your Markdown text, without pasting bulky HTML.
Use emoticon-like strings like `:fa-hot-mug:` to place the corresponding FontAwesome markup in your text flow.

### How to use

Include FontAwesome v6.6 CSS/assets to your DOM, then add `fontawesome_in_markdown` to your Markdown:

```python
from markdown import Markdown

markdown = Markdown(extensions=['fontawesome_in_markdown']
```

Now you can try some trickery:

```python
markdown.convert('I ♥ :fa-hot-mug:')
```

will output

```html
<p>i ♥ <i class="fa-solid fa-hot-mug"></i></p>
```

and

```python
markdown.convert('i ♥ :far fa-star: fa-x3')
```

will output

```html
<p>i ♥ <i class="fa-regular fa-fontawe fa-x3"></i></p>
```

### Known issues

The `light` prefix, althought supported in code, won't work because FontAwesome doesn't currently expose `light` icons in their metadata file.

### Credits

This extension is a fork of [`fontawesome-markdown` by `bmcorser`](http://bmcorser.github.com/fontawesome-markdown).  
For some reasons, the original repository is abandoned, so I decided to publish this updated version, after waiting for a PR to be accepted.

Should the original author come back in the future, to maintain the original package, I will probably merge it back. In the meantime this should be a valid dropdown replacement.

### Contributions

I'll try my best to keep this repo up to date, reviewing and accepting contributions, but I'm not an expert Pythonista myself. Feel free to send in PRs as long as they describe the scope clearly, to ease the review process.
