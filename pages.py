import os
from airium import Airium
from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = os.getenv('OUTPUT_DIR')
FILENAME_INDEX = OUTPUT_DIR + "/index.html"
FILENAME_CONTACT = OUTPUT_DIR + "/contact/index.html"
FILENAME_SOCIALS = OUTPUT_DIR + "/socials/index.html"
FILENAME_ERR_404 = OUTPUT_DIR + "/404.html"

filenames = [FILENAME_INDEX, FILENAME_CONTACT, FILENAME_SOCIALS, FILENAME_ERR_404]


def write_head(b):
    with b.head():
        b.meta(charset="utf-8")
        b.meta(name="viewport", content="width=device-width, initial-scale=1.0")
        b.link(href="/apple-touch-icon.png", rel="apple-touch-icon")
        b.link(href="/favicon-32x32.png", rel="icon", type="image/png", sizes="32x32")
        b.link(href="/favicon-16x16.png", rel="icon", type="image/png", sizes="16x16")
        b.link(href="/site.webmanifest", rel="manifest")
        b.title(_t="tabla.ng")
        b.link(href="/static/css/modern-normalize.css", rel="stylesheet")
        b.link(href="/static/css/style.css", rel="stylesheet")
        b.link(href="/static/css/dark.css", rel="stylesheet", id="darksheet", disabled="disabled")
        b.script(src="/static/js/htmx.min.js")
        b.script(src="/static/js/_hyperscript.min.js")
    return b

def write_footer(b):
    with b.div(klass="footer"):
        b.hr()
        with b.p():
            b("Powered by")
            b.a(_t="HTMX", href="https://htmx.org")
            b("and")
            b.a(_t="Hyperscript", href="https://hyperscript.org", klass="a-period")
            b.a(_t="No Rights Reserved", href="https://creativecommons.org/publicdomain/zero/1.0/deed.en", klass="a-period")
    return b


def index():
    index = Airium()

    index('<!DOCTYPE html>')
    with index.html():
        index = write_head(index)
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
                        index.img(src="/static/peanuts.jpg", _="init transition my opacity to 100% over 2 seconds "
                                +"on click toggle .inverted on me", style="transition: all 250ms ease-in")
                    with index.p():
                        index("Hi, I am Karlo Tablang.")
                    with index.div():
                        index.a(_t="Contact", _="on click if I match .active remove .active from me then hide #values else remove .active from <a/> then add .active to me then show #values end", **{"hx-get":"/contact/","hx-target":"#values"})
                        index("/")
                        index.a(_t="Socials", _="on click if I match .active remove .active from me then hide #values else remove .active from <a/> then add .active to me then show #values end", **{"hx-get":"/socials/","hx-target":"#values"})
                    index.div(id="values")
                index = write_footer(index)

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


def err_404():
    b = Airium()

    b('<!DOCTYPE html>')
    with b.html():
        b = write_head(b)
        with b.body():
            with b.div(id="container"):
                with b.div(id="header"):
                    with b.h1():
                        b.a(_t="tabla.ng", href="/")
                        with b.label(klass="switch"):
                            b.input(type="checkbox", id="toggler")
                            b.span(klass="slider")
                        b.script(src="/static/js/dark.js")
                with b.div(id="content"):
                    with b.p():
                        b.img(src="/static/peanuts.jpg", _="init transition my opacity to 100% over 2 seconds\
                                on click toggle my .inverted", style="transition: all 250ms ease-in")
                    with b.p():
                        b("404 Not Found, Sadly")
                b = write_footer(b)

    return b


pages = [
    ('index', FILENAME_INDEX, index()),
    ('contact', FILENAME_CONTACT, contact()),
    ('socials', FILENAME_SOCIALS, socials()),
    ('404', FILENAME_ERR_404, err_404())
]


def write():
    for filename in filenames:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    for page in pages:
        with open(page[1], 'wb') as f:
            f.write(bytes(page[2]))