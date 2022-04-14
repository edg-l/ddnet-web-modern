# Modern ddnet.tw web

A rework of the ddnet.tw website with the objective to make it more maintainable by others and modernize it.

It will still work like the previous website where everything is rendered beforehand to files.

The previous website used python `print` statements to render manually all HTML, here we will use jinja2 templates.

## Package manager
To make local development easier, we use [pipenv](https://pipenv.pypa.io/en/latest/) to manage the dependencies.