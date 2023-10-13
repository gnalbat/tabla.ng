import os
from airium import Airium
from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = os.getenv('OUTPUT_DIR')
FILENAME_INDEX = OUTPUT_DIR + "/index.html"
FILENAME_CONTACT = OUTPUT_DIR + "/contact/index.html"
FILENAME_SOCIALS = OUTPUT_DIR + "/socials/index.html"

filenames = [FILENAME_INDEX, FILENAME_CONTACT, FILENAME_SOCIALS]

def index():
    index = Airium()

    index('<!DOCTYPE html>')
    with index.html():
        with index.head():
            index.meta(charset="utf-8")
            index.meta(name="viewport", content="width=device-width, initial-scale=1.0")
            index.link(href="/apple-touch-icon.png", rel="apple-touch-icon")
            index.link(href="/favicon-32x32.png", rel="icon", type="image/png", sizes="32x32")
            index.link(href="/favicon-16x16.png", rel="icon", type="image/png", sizes="16x16")
            index.link(href="/site.webmanifest", rel="manifest")
            index.title(_t="tabla.ng")
            index.link(href="/static/css/modern-normalize.css", rel="stylesheet")
            index.link(href="/static/css/style.css", rel="stylesheet")
            index.link(href="/static/css/dark.css", rel="stylesheet", id="darksheet")
            index.script(src="/static/js/htmx.min.js")
            index.script(src="/static/js/_hyperscript.min.js")
        with index.body():
            with index.div(id="container"):
                with index.div(id="header"):
                    with index.h1():
                        index.a(_t="tabla.ng", href="/")
                        with index.label(klass="switch"):
                            index.input(type="checkbox", id="toggler")
                            index.span(klass="slider")
                        index.script(src="/static/js/dark.js")
                with index.div(id="content"):
                    with index.p():
                        index.img(src="/static/peanuts.jpg", _="init transition my opacity to 100% over 2 seconds\
                                on click toggle my .inverted", style="transition: all 250ms ease-in")
                    with index.p():
                        index("Hi, I am Karlo Tablang.")
                    with index.div():
                        index.a(_t="Contact", **{"hx-get":"/contact/","hx-target":"#values"})
                        index("/")
                        index.a(_t="Socials", **{"hx-get":"/socials/","hx-target":"#values"})
                    index.div(id="values")
                with index.div(klass="footer"):
                    index.hr()
                    with index.p():
                        index("Powered by")
                        index.a(_t="HTMX", href="https://htmx.org")
                        index("and")
                        index.a(_t="Hyperscript", href="https://hyperscript.org", klass="a-period")
                        index.a(_t="No Rights Reserved", href="https://creativecommons.org/publicdomain/zero/1.0/deed.en", klass="a-period")

    return index


def contact():
    b = Airium()

    with b.ul():
        with b.li():
            b.a(href="mailto:karlo@tabla.ng", _t="karlo@tabla.ng")
    
    return b


def socials():
    b = Airium()

    with b.ul():
        with b.li():
            b.a(href="https://github.com/gnalbat", _t="GitHub", rel="noreferrer", target="_blank")
        with b.li():
            b.a(href="https://linkedin.com/in/kmtablang", _t="LinkedIn", rel="noreferrer", target="_blank")
    return b


pages = [
    ('index', FILENAME_INDEX, index()),
    ('contact', FILENAME_CONTACT, contact()),
    ('socials', FILENAME_SOCIALS, socials())
]


def write():
    for filename in filenames:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    for page in pages:
        with open(page[1], 'wb') as f:
            f.write(bytes(page[2]))