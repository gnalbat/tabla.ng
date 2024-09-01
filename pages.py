import os
from airium import Airium
from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = os.getenv('OUTPUT_DIR')
FILENAME_INDEX = OUTPUT_DIR + "/index.html"
FILENAME_ABOUT = OUTPUT_DIR + "/about/index.html"
FILENAME_CONTACT = OUTPUT_DIR + "/contact/index.html"
FILENAME_ERR_404 = OUTPUT_DIR + "/404.html"

filenames = [FILENAME_INDEX, FILENAME_ABOUT, FILENAME_CONTACT, FILENAME_ERR_404]

HS_IMAGELOAD = "init transition my opacity to 100% over 2 seconds"

SOCIAL_LINKS = [
    ["linkedin",    "https://linkedin.com/in/ktablang"],
    ["github",      "https://github.com/gnalbat"],
    ["pexels",      "https://www.pexels.com/@karlo-tablang-762366984/"],
    ["portfolio",   "https://gnalb.at"],
    ["oh, karlo",   "https://ok.tabla.ng"]
]

def write_head(b):
    with b.head():
        b.meta(charset="utf-8")
        b.meta(name="viewport", content="width=device-width, initial-scale=1.0")
        b.link(href="/apple-touch-icon.png", rel="apple-touch-icon")
        b.link(href="/favicon-32x32.png", rel="icon", type="image/png", sizes="32x32")
        b.link(href="/favicon-16x16.png", rel="icon", type="image/png", sizes="16x16")
        b.link(href="/site.webmanifest", rel="manifest")
        b.title(_t="karlo tablang")
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
                        index.img(src="/static/peanuts.jpg", _=HS_IMAGELOAD, style="transition: all 250ms ease-in")
                    with index.p():
                        index("hi! i'm karlo tablang.")
                    with index.div(_="on htmx:beforeOnLoad take .active from .tab for event.target", **{"hx-target":"#tab-content"}):
                        index.a(klass="tab", _t="about", **{"hx-get":"/about/",})
                        index("/")
                        index.a(klass="tab", _t="contact", **{"hx-get":"/contact/"})
                    index.div(id="tab-content")
                index = write_footer(index)

    return index


def about():
    b = Airium()

    b.p(_t="i do stuff.")
    b.p(_t="you <i>may</i> find me at the following:")

    with b.ul():
        for link in SOCIAL_LINKS:
            with b.li():
                b.a(href=link[1], _t=link[0], rel="noreferrer", target="_blank")
        
    return b


def contact():
    b = Airium()

    with b.ul():
        with b.li():
            b("get in touch:")
            b.a(href="mailto:hello@tabla.ng", _t="hello@tabla.ng")
        with b.li():
            b("work opportunities:")
            b.a(href="mailto:work@tabla.ng", _t="work@tabla.ng")
        with b.li():
            b("correspondence:")
            b.a(href="mailto:karlo@tabla.ng", _t="karlo@tabla.ng")
    
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
                        b.img(src="/static/peanuts.jpg", _=HS_IMAGELOAD, style="transition: all 250ms ease-in")
                    with b.p():
                        b("404 not found")
                b = write_footer(b)

    return b


pages = [
    ('index',   filenames[0],   index()),
    ('about',   filenames[1],   about()),
    ('contact', filenames[2],   contact()),
    ('404',     filenames[3],   err_404())
]


def write():
    for filename in filenames:
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    for page in pages:
        with open(page[1], 'wb') as f:
            f.write(bytes(page[2]))