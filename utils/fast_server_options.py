from reactpy import html
from reactpy.backend.fastapi import Options

PAGE_HEADER_TITLE  = 'ReactPy GitHub Buttons'

# https://picocss.com/docs/

PICO_CSS = {
        'rel': 'stylesheet',
        'href': 'https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css',
        'crossorigin': 'anonymous'
    }

GITHUB_BUTTONS_CSS = {
        'rel': 'stylesheet',
        'href': 'https://buttons.github.io/css/app.48c6bc16.css'
    }

META_VIEWPORT = {
    'name': "viewport",
    'content': "width=device-width",
    'initial-scale': 1
    }

META_COLOR = {
    'theme-color': "viewport",
    'content': "#000000"
    }

DEFAULT_OPTIONS=Options(
    head=html.head(
        html.meta(META_VIEWPORT),
        html.meta(META_COLOR),
        html.title(PAGE_HEADER_TITLE),
    )
)


PICO_OPTIONS=Options(
    head=html.head(
        html.meta(META_VIEWPORT),
        html.meta(META_COLOR),
        html.link(PICO_CSS),
        html.title(PAGE_HEADER_TITLE),
    )
)

